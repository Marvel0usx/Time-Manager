# A sub-program uesd to communicate with the database

import sqlite3

# Setup work environment
def create_database (database_name):
    database = sqlite3.connect (database_name)
    database.execute ("CREATE TABLE user_information (username VARCHAR(30) NOT NULL PRIMARY KEY, password VARCHAR(30) NOT NULL);")
    database.commit ()
    database.close ()
    # 0 -> success
    return 0

# Check username
def check_username (database_name,username):
    database = sqlite3.connect (database_name)
    number_of_result = len (database.execute ("SELECT username FROM user_information WHERE username = '%s';" % (username)).fetchall ())
    database.close ()
    # 0 -> found username; 1 -> username not found
    if number_of_result != 0:
        return 0
    else:
        return 1

# Check password
def check_password (database_name,username,password):
    database = sqlite3.connect (database_name)
    correct_password = database.execute ("SELECT username,password FROM user_information WHERE username = '%s';" % (username)).fetchall ()
    database.close ()
    correct_password = correct_password[0][1]
    # 0 -> password correct; 1 -> password incorrect
    if correct_password == password:
        return 0
    else:
        return 1

# Create account
def create_account (database_name,username,password):
    database = sqlite3.connect (database_name)
    database.execute ("INSERT INTO user_information VALUES ('%s','%s');" % (username,password))
    database.execute ("CREATE TABLE %s_schedules (date_start CHAR(14) NOT NULL, date_end CHAR(14) NOT NULL, event_level INT NOT NULL, event_name VARCHAR(30) NOT NULL, event_location VARCHAR(30), Note TEXT, PRIMARY KEY (date_start,date_end));" % (username))
    database.commit ()
    database.close ()

# Change username
def change_username (database_name,username,new_username):
    database = sqlite3.connect (database_name)
    database.execute ("UPDATE user_information SET username = '%s' WHERE username = '%s';" % (new_username,username))
    database.execute ("ALTER TABLE %s RENAME TO %s" % (username + "_schedules",new_username + "_schedules"))
    database.commit ()
    database.close ()

# Change password
def change_password (database_name,username,password):
    database = sqlite3.connect (database_name)
    database.execute ("UPDATE user_information SET password = '%s' WHERE username = '%s';" % (password,username))
    database.commit ()
    database.close ()

# Delete account
def delete_account (database_name,username):
    database = sqlite3.connect (database_name)
    database.execute ("DELETE FROM user_information WHERE username = '%s'" % (username))
    database.execute ("DROP TABLE %s_schedules" % (username))
    database.commit ()
    database.close ()