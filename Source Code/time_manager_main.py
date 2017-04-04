# Main program to interconnect each parts of the program

import os
import datetime
import cmd_io
import database_io

# Constents
database_name = "time_manager.db"
username = ""
action_number = "0"
program_end = False

# Startup check
cmd_io.initialization (database_name)

# Action tree
# Login process
while not program_end:
    if action_number[0] == "0":
        if action_number == "0":
            action_number = cmd_io.user_login_menu ()
        elif action_number == "01":
            action_number,username = cmd_io.login_account (database_name)
        elif action_number == "02":
            action_number,username = cmd_io.create_account (database_name)
        else:
            print (">> Ending program...")
            program_end = True
    if action_number[0] == "1":
        cmd_io.header ()
        print (">> Welcome back %s" % (username))
        input ()

# End of the program
print (">> Program ended...")
