

import Varified_gmail_and_password

import json
import os


all_users_dict = {}
 
def get_user_data():
    users_file = "/var/www/voting-data/users.json" if os.path.exists("/var/www/voting-data") else "Varified_gmail_and_password/users.json"
    
    try:
        with open(users_file, "r") as f:
            users = json.load(f)
            list_of_dicts = {email: details["password"] for email, details in users.items()}
            return list_of_dicts
    except Exception as e:
        print(f"Error loading user data: {e}")
        return {}