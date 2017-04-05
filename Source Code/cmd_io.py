# A sub-program used to achieve all the formated output of the program

import os
import datetime
import database_io

# Uniformed header
def header ():
    file = open ("ASCII_logo.txt","r")
    logo = file.read ()
    file.close ()
    os.system ("cls")
    print (75 * "=")
    print (logo)
    print (75 * "=")

# Uniformed header with username and date
def header_user_date (username):
    header ()
    date = str (datetime.datetime.now ())
    print ("Current user: " + format (username,"<30") + 14 * " " + "Today: %s/%s/%s" % (date[0:4],date[5:7],date[8:11]) + "\n")

# Start check
def initialization (database_name):
    header ()
    print (">> Initializing the program...\n>> Checking reuqired files...")
    if not os.path.exists (database_name):
        print ("\a>> File not found\n>> Creating needed files...")
        if database_io.create_database (database_name) == 0:
            print (">> Files created")
            input ("   (Press 'enter' key to continue...)")

# Action branch 0
# Action 00 -> Action branch 0 menu
def action_0_menu ():
    header ()
    print (">> 1. Login to a account\n   2. Create a new account\n   3. Exite the program")
    user_option = ""
    while user_option != '1' and user_option != '2' and user_option != '3':
        user_option = input (">> Option: ")
    if user_option == '1':
        return "01"
    elif user_option == '2':
        return "02"
    else:
        return "exit"

# Get a valid input
def valid_input (message):
    user_input = ""
    while user_input == "" or len (user_input) > 30:
        user_input = input (message)
    return user_input

# Action 01 -> Login to account
def login_account (database_name):
    header ()
    username = valid_input (">> Enter your username below:\n   ")
    state = database_io.check_username (database_name,username)
    if state == 0:
        password = valid_input (">> Enter your password below:\n   ")
        state = database_io.check_password (database_name,username,password)
        if state == 1:
            for times in range (3):
                print (">> Password incorrect")
                password = valid_input (">> Enter your password below (%s trys remain):\n   " % (3 - times))
                state = database_io.check_password (database_name,username,password)
                if state == 0:
                    break
        if state == 1:
            print (">> Access denied")
            input ("   (Press 'enter' key to continue...)")
            return "exit","",""
        else:
            return "100",username,username + "_schedules"
    else:
        print (">> Username not found in database")
        user_option = ""
        while user_option != 'y' and user_option != 'n':
            user_option = input (">> Would you like to create a new account? (y/n): ").lower ()
        if user_option == 'y':
            return "02","",""
        else:
            print (">> You can not access the database without a account")
            input ("   (Press 'enter' key to continue...)")
            return "exit","",""

# Action 02 -> Create a new account
def create_account (database_name):
    header ()
    print (">> You are now creating a new account in our database...")
    username = valid_input (">> Enter a username below (up to 30 characters):\n   ")
    state = database_io.check_username (database_name,username)
    while state != 1:
        print (">> Usernam not available")
        username = valid_input (">> Enter a username below (up to 30 characters):\n   ")
        state = database_io.check_username (database_name,username)
    print (">> Username available")
    password = valid_input (">> Enter a password below (up to 30 characters):\n   ")
    re_password = valid_input (">> Renter your password below:\n   ")
    while re_password != password:
        print (">> Two times are different")
        re_password = valid_input (">> Renter your password below:\n   ")
    database_io.create_account (database_name,username,password)
    return "100",username,username + "_schedules"

# Action branch 1
# Action 10 -> Action branch 1 menu
def action_1_menu (username):
    header_user_date (username)
    print (">> 1. Account management\n   2. Schedules management\n   3. Signout for this account\n   4. Exit")
    user_option = ""
    while user_option != '1' and user_option != '2' and user_option != '3' and user_option != '4':
        user_option = input (">> Option: ")
    if user_option == '1':
        return "110"
    elif user_option == '2':
        return "120"
    elif user_option == '3':
        return "130"
    else:
        return "exit"

# Action 110 -> Account management menu (befor login)
def action_11_menu (database_name,username):
    header_user_date (username)
    print (">> You are now changing your account information...")
    password = valid_input (">> For security reason, enter your current password below:\n   ")
    state = database_io.check_password (database_name,username,password)
    if state == 1:
        for times in range (3):
            print (">> Password incorrect")
            password = valid_input (">> Enter your password below (%s trys remain):\n   " % (3 - times))
            state = database_io.check_password (database_name,username,password)
            if state == 0:
                break
    if state == 1:
        print (">> Sorry, we cannot let you change your account information")
        input ("   (Press 'enter' key to continue...)")
        return "100"
    else:
        header_user_date (username)
        print (">> 1. Change username\n   2. Change password\n   3. Delet account\n   4. Back")
        user_option = ""
        while user_option != '1' and user_option != '2' and user_option != '3' and user_option != '4':
            user_option = input (">> Option: ")
        if user_option == '1':
            return "111"
        elif user_option == '2':
            return "112"
        elif user_option == '3':
            return "113"
        else:
            return "100"

# Action 111 -> Change username
def change_username (database_name,username):
    header_user_date (username)
    print (">> Changeing your username...")
    new_username = valid_input (">> Enter a new username below (up to 30 characters):\n   ")
    state = database_io.check_username (database_name,new_username)
    while state != 1:
        print (">> Usernam not available")
        new_username = valid_input (">> Enter a new username below (up to 30 characters):\n   ")
        state = database_io.check_username (database_name,new_username)
    print (">> Username available")
    database_io.change_username (database_name,username,new_username)
    print (">> Your username as been updated")
    input ("   (Press 'enter' key to continue...)")
    return "100",new_username,new_username + "_schedules"

# Action 112 -> Change password
def change_password (database_name,username):
    header_user_date (username)
    print (">> Changing your password...")
    password = valid_input (">> Enter a new password below (up to 30 characters):\n   ")
    re_password = valid_input (">> Renter your new password below:\n   ")
    while re_password != password:
        print (">> Two times are different")
        re_password = valid_input (">> Renter your new password below:\n   ")
    database_io.change_password (database_name,username,password)
    print (">> Your password as been updated")
    input ("   (Press 'enter' key to continue...)")
    return "100"

# Action 113 -> Delet account
def delet_account (database_name,username):
    header_user_date (username)
    print (">> Deleting your acctoun...")
    print (">> " + format ("<<< WARING >>>","^72"))
    user_option = ""
    while user_option != 'y' and user_option != 'n':
        user_option = input (">> You are now tring to delet your account, this process is irreversible.\n   Are you sure you want to delet your account along with all information?\n   (y/n): ").lower ()
    if user_option == 'y':
        print (">> Deleting your account...")
        database_io.delete_account (database_name,username)
        print (">> Account deleted")
        user_option = ""
        while user_option != 'y' and user_option != 'n':
            user_option = input (">> Would you like to create a new account? (y/n): ").lower ()
        if user_option == 'y':
            return "02"
        else:
            return "00"
    else:
        return "100"

# There should be Action 120

# Action 130 -> Signout from current account
def signout ():
    return "00","",""