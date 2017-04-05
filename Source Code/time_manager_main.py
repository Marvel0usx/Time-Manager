# Main program to interconnect each parts of the program

import os
import datetime
import cmd_io
import database_io

# Constents
database_name = "time_manager.db"
username = ""
user_table_name = ""
action_number = "00"
program_end = False

# Startup check
cmd_io.initialization (database_name)

# Action tree
while not program_end:
    if action_number == "exit":
        break
    # Action branch 0
    if action_number[0] == "0":
        if action_number == "00":
            action_number = cmd_io.action_0_menu ()
        elif action_number == "01":
            action_number,username,user_table_name = cmd_io.login_account (database_name)
        elif action_number == "02":
            action_number,username,user_table_name = cmd_io.create_account (database_name)
    # Action branch 1
    if action_number[0] == "1":
        if action_number == "100":
            action_number = cmd_io.action_1_menu (username)
        elif action_number[1] == "1":
            if action_number == "110":
                action_number = cmd_io.action_11_menu (database_name,username)
            elif action_number == "111":
                action_number,username,user_table_name = cmd_io.change_username (database_name,username)
            elif action_number == "112":
                action_number = cmd_io.change_password (database_name,username)
            else:
                action_number = cmd_io.delet_account (database_name,username)
        elif action_number[1] == "2":
            print (">> Accessing schedules management...")
            input ()
        elif action_number[1] == "3":
            action_number,username,user_table_name = cmd_io.signout ()
# End of the program
print (">> Exiting program...")