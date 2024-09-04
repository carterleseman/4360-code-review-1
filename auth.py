import json
from user import User
from account import Account
from message import Message

class Auth:
    def __init__(self):
        self.message = Message()

    def login(self, username, password):
        try:
            with open('db.json', 'r') as file:
                data = json.load(file)
                users = data.get('users', [])
                
            for user in users:
                if user.get('name') == username and user.get('password') == password:
                    accounts = {
                        account['accountNumber']: Account(account['balance'])
                        for account in user.get('accounts', [])
                    }
                    return User(user['name'], accounts)
                
            self.message.print("name or password not found")
            return None
        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.message.print(f"Error loading database: {e}")
            return None