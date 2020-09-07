#!/usr/bin/env python3.6

from user import User
from accounts import Credentials
import random
import string


def create_account(fullname, username, password):
    """
    Function for creating a new user account
    """

    new_user = User(fullname, username, password)
    return new_user


def save_user(user):
    '''
    Function to save new user credentials
    '''
    User.save_user(user)


def verify_user_login(user_name, user_password):
    """
    funtion to verify user input and log in accout details
    """

    account_exist = User.verify_user(user_name, user_password)
    # print("verify_user_login")
    # print(account_exist)
    return account_exist


def create_new_credentials(acc_name, acc_username, acc_password):
    """
    Funtion for creating new user credentials
    """
    new_user_credentials = Credentials(acc_name, acc_username, acc_password)
    return new_user_credentials


def save_new_user_credentials(credential):
    """
    funtion to save user credentials
    """

    credential.save_existing_acc()


def del_user_credentials(credential):
    """
    funtion to delete user credentials
    """

    credential.delete_user_credentials()


def dis_user_credentials():
    """
    funtion that returns all saved contacts
    """

    return Credentials.display_user_credentials()


def generate_password():
    """Funtion that generates random password for the user"""

    gen_password = Credentials.generate_password()
    return gen_password


def main():
    command = ''
    while True:
        print("""
Welcome to password Locker!
Use the following commands to procceed:
  New - New user
  Log - Log into account
  Quit - Terminate process
      """)
        command = input("Please choose a command : ").lower().strip()

        if command == 'new':
            print('\n')
            fullname = input("Enter full name : ")
            user_name = input("Enter username : ")
            password = input("Enter password : ")
            confirm_password = input("Confirm password : ")
            save_user(create_account(
                fullname, user_name, password))
            print('*'*50)
            print(
                f"Welcome {user_name}. Your account has been created succesfully!")
            print('*'*50)
            print('\n')

            while password != confirm_password:
                print("Sorry. Password didn't not match. Please \n")
                password = input("Enter password : ")
                confirm_password = input("Confirm password : ")
            else:
                print('*'*50)
                print(
                    "Proceed to Login to your account. Use the command 'log' to login. \n")
                print('*'*50)
                # login_details = create_account(fullname, user_name, password)

        elif command == 'log':
            username_input = input("Username : ")
            password_input = input("Password : ")
            print('\n')
            log_in = verify_user_login(username_input, password_input)
            print(log_in)

            if log_in == False:
                print(
                    "Sorry. The account does not exist. Please try again or create an account to access Password Locker\n")

            else:
                print("Login Successful! \n")
                print("*"*50)
                print(
                    f"Your user name is {username_input} and password {password_input} \n")
                print("*"*50)

                while True:
                    print(
                        "Proceed to manage your account. Use the following short-codes to navigate through the application")
                    print("""
          nw - create new account credentials
          vw - view existing credentials
          dl - delete account credentials
          ex - exit
          \n
                      """)
                    short_code_choice = input(
                        "Please choose a command : ").lower().strip()
                    if short_code_choice == 'nw':
                        print("Fill in the account details you want to store")
                        account_name = input("Account name : ")
                        account_username = input("Account username : ")

                        while True:
                            print("""
        Would you like to use your own password or a random generated password?
        Use short-codes:
            my - your password choice
            gp - to generate password
        """)
                            user_choice = input("> ").lower().strip()
                            if user_choice == 'my':
                                user_choice_pass = input("Your password :")
                                break
                            elif user_choice == 'gp':
                                user_choice_pass = generate_password()
                                break
                            else:
                                print(
                                    "Sorry. I didn't catch that. Try again please...")

                        save_new_user_credentials(create_new_credentials(
                            account_name, account_username, user_choice_pass))
                        print('*'*50)
                        print(
                            f"User credential : Page-name : {account_name} Username : {account_username} Password : {user_choice_pass} created.")
                        print('*'*50)
                        print("\n")

                    elif short_code_choice == 'vw':
                        if dis_user_credentials():
                            print("Here is a list of your current credentials : ")
                            print('*'*50)
                            for credential in dis_user_credentials():
                                print(
                                    f"Account name : {credential.acc_name}\nUsername : {account_username}\nPassword : {user_choice_pass}")
                                print('*'*50)
                                print("\n")
                        else:
                            print('*'*50)
                            print(
                                "Sorry. You don't seem to have any acounts yet. Would you like to create an account?")
                            print('*'*50)
                            print("\n")

                    elif short_code_choice == 'dl':
                        print("What would you like to delete?")

                    else:
                        print("Thank you!")
                        break

        elif command == 'quit':
            print("Thank you for using Password Locker. See you soon!")
            break
        else:
            print("Sorry I didn't understand that command. Please enter a valid command.")


if __name__ == '__main__':
    main()
