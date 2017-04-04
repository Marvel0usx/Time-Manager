# A sub-program used to achieve all the formated output of the program

import os
import datetime
import database_io

# Uniformed header
def header ():
    # Open file
    file = open ("ASCII_logo.txt","r")
    logo = file.read ()
    file.close ()
    # Output header
    os.system ("cls")
    print (65 * "=")
    print (logo)
    print (65 * "=")

# Start check
def initialization (database_name):
    header ()
    print (">> Initializing the program...\n>> Checking reuqired files...")
    if not os.path.exists (database_name):
        print ("\a>> File not found\n>> Creating needed files...")
        if database_io.create_database (database_name) == 0:
            print (">> File created")

# User login
def user_login_menu ():
    header ()
    # Print option
    print (">> 1. Login to a account\n   2. Create a new account\n   3. Exite the program")
    user_option = ""
    while user_option != '1' and user_option != '2' and user_option != '3':
        user_option = input (">> Option: ")
    action_number = "0" + user_option
    return action_number

# Login to account
def login_account (database_name):
    header ()
    username = ""
    while username == "":
        username = input (">> Enter your username:\n>> ")
    state = database_io.check_username (database_name,username)
    if state == 0:
        password = ""
        while password == "":
            password = input (">> Enter your password:\n>> ")
        state = database_io.check_password (database_name,username,password)
        if state == 1:
            for times in range (3):
                print (">> Password incorrect")
                password = ""
                while password == "":
                    password = input (">> Enter your password (%s trys remain):\n>> " % (3 - times))
                state = database_io.check_password (database_name,username,password)
                if state == 0:
                    break
        if state == 1:
            print (">> Access denied")
            input ("   (Press 'enter' key to exit the program...)")
            return "03",""
        else:
            return "1",username
    else:
        print (">> Username not found in database")
        user_option = ""
        while user_option != 'y' and user_option != 'n':
            user_option = input (">> Would you like to create a new account? (y/n): ").lower ()
        if user_option == 'y':
            return "02",""
        else:
            print (">> You can not access the database without a account")
            input ("   (Press 'enter' key to continue...)")
            return "03",""

# Create a new account
def create_account (database_name):
    header ()
    print (">> You are now creating a new account in our database...")
    username = ""
    while username == "":
        username = input (">> Enter a username below (up to 30 characters):\n>> ")
    state = database_io.check_username (database_name,username)
    while state != 1:
        print (">> Usernam not available")
        username = ""
        while username == "":
            username = input (">> Enter a username below (up to 30 characters):\n>> ")
        state = database_io.check_username (database_name,username)
    print (">> Username available")
    password = ""
    while password == "":
        password = input (">> Enter a password below (up to 30 characters):\n>> ")
    re_password = ""
    while re_password == "":
        re_password = input (">> Renter your password below:\n>> ")
    while re_password != password:
        print (">> Two times are different")
        re_password = ""
        while re_password == "":
            re_password = input (">> Renter your password below:\n>> ")
    database_io.create_account (database_name,username,password)
    return "1",username