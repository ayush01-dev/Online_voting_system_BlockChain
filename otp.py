import smtplib
import random
import time

# Step 1: Generate OTP and timestamp
def generate_otp():
    otp = str(random.randint(100000, 999999))
    timestamp = time.time()
    return otp, timestamp

# Step 2: Send OTP via Gmail
def send_otp(receiver_email, otp):
    sender_email = "420la007@gmail.com"
    sender_password = "otvr frxa rpxl ltjs"  # Use App Password

    message = f"Subject: Your OTP Verification Code\n\nYour OTP is: {otp}\n(This OTP is valid for 2 minutes.)"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print(f"OTP sent to {receiver_email}")
    except Exception as e:
        print("Failed to send email:", e)

# Step 3: Verify OTP with expiry check
def verify_otp(sent_otp, sent_time):
    user_otp = input("Enter the OTP sent to your email: ")
    current_time = time.time()
    if current_time - sent_time > 120:
        print("⏰ OTP has expired!")
    elif user_otp == sent_otp:
        print("✅ OTP Verified Successfully!")
    else:
        print("❌ Invalid OTP!")

# Main Program
if __name__ == "__main__":
    email = input("Enter your Gmail address: ")
    otp, timestamp = generate_otp()
    send_otp(email, otp)
    verify_otp(otp, timestamp)
