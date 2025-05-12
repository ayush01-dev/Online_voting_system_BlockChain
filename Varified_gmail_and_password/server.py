from flask import Flask, render_template, request, redirect, session
import time, json
from otp import generate_otp, send_otp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DB_FILE = "Varified_gmail_and_password/users.json"

# Load users
try:
    with open(DB_FILE, 'r') as f:
        users = json.load(f)
except:
    users = {}

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        email = request.form["email"]
        password = request.form["password"]

        if email in users:
            return "⚠️ This Gmail is already registered!"

        otp, timestamp = generate_otp()
        send_otp(email, otp)

        # Store in session for verification
        session.update({
            "email": email,
            "password": password,
            "otp": otp,
            "time": timestamp,
            "name": name,
            "age": age
        })
        return redirect("/verify")
    return render_template("register.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_otp = request.form["otp"]
        sent_otp = session["otp"]
        sent_time = session["time"]

        if time.time() - sent_time > 120:
            return "⏰ OTP expired. Go back and try again."
        elif user_otp == sent_otp:
            email = session["email"]
            users[email] = {
                "name": session["name"],
                "age": session["age"],
                "password": session["password"]
            }
            with open(DB_FILE, "w") as f:
                json.dump(users, f, indent=4)
            send_success_email(email, session["name"])
            return "✅ Registered successfully !"
        else:
            return "❌ Incorrect OTP!"
    return render_template("verify.html")

# ✉️ Send welcome mail after successful registration
# def send_success_email(receiver_email, name):
#     import smtplib
#     sender_email = "420la007@gmail.com"
#     sender_password = "otvr frxa rpxl ltjs"  # App password
#
#     message = f"""Subject: Welcome to Our App 🎉
#
# Hello {name},
#
# 🎉 Congratulations! You have successfully registered.
# We are excited to have you on board.
#
# Stay tuned for more updates.
#
# Warm regards,
# The Team
# """
#
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, receiver_email, message)
#         server.quit()
#         print(f"Confirmation email sent to {receiver_email}")
#     except Exception as e:
#         print("Failed to send confirmation email:", e)


def send_success_email(receiver_email, name):
    import smtplib
    sender_email = "420la007@gmail.com"
    sender_password = "otvr frxa rpxl ltjs"  # App password

    message = f"""Subject: Welcome to Our App 🎉

Hello {name},

🎉 Congratulations! You have successfully registered.
We are excited to have you on board.

Stay tuned for more updates.

Warm regards,
The Team
"""

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
        server.quit()
        print(f"Confirmation email sent to {receiver_email}")
    except smtplib.SMTPException as e:
        print("SMTP error occurred:", e)
    except Exception as e:
        print("Failed to send confirmation email:", e)


if __name__ == "__main__":
    app.run(debug=True)
