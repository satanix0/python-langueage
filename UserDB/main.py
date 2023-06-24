import sys
from dbhelper import DBhelper


class Apped:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input(
            """1. Enter 1 to Register\n2. Enter 2 to Login\n::""")

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(100)

    def register(self):
        # Take details input
        username = input("Enter Username: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        # check successful registration
        success = self.db.create_user(username, email, password)

        if success:
            print("Registration Successful")
        else:
            print("Registration failed")

        self.menu()

    def login(self):
        email = input("Enter email: ")
        password = input("Enter Password: ")
        data = self.db.search(email, password)


obj = Apped()
