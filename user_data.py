

import Varified_gmail_and_password
import json

all_users_dict = {}
def get_user_data():
    with open("Varified_gmail_and_password/users.json", "r") as f:
        users = json.load(f)
        data = json.dumps(users, indent=4)
    # print(data)

    list_of_dicts = [{"email": email, **details} for email, details in users.items()]
    # print(list_of_dicts)
    list_of_dicts = {email: details["password"] for email, details in users.items()}
    # print(list_of_dicts)
    all_users_dict = list_of_dicts
    return all_users_dict


