import getpass
import pickle
import os

PASSWORD_FILE = 'passwords.pkl'

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'rb') as f:
            return pickle.load(f)
    else:
        return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'wb') as f:
        pickle.dump(passwords, f)

def add_password(passwords):
    site = input("Enter the name of the site or service: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    passwords[site] = (username, password)
    save_passwords(passwords)

def view_password(passwords):
    site = input("Enter the name of the site or service: ")
    if site in passwords:
        print("Username: ", passwords[site][0])
        print("Password: ", passwords[site][1])
    else:
        print("No password stored for that site.")

def password_manager():
    passwords = load_passwords()

    while True:
        print("What would you like to do?")
        print("1. Add a password")
        print("2. View a password")
        print("3. Quit")
        choice = input("> ")
        
        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            view_password(passwords)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    password_manager()
