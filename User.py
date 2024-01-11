# User.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print(f"Username: {self.username}, Email: {self.email}")
