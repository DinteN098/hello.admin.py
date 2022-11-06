#This are the users who are on the system

usernames = ['Admin', 'Hank', 'David', 'Mike', 'Sam']

#This is the user logging in

user_logging = 'admin'

#This will change the first letter of the the username to a capital letter

user_logging_cap = user_logging.title()

#This function will check the whether the user is the admin

if user_logging_cap == usernames[0]:
    print(f"Hello {usernames[0]}, would you like to see a status report?")

#This function will start if the user is not the admin

if user_logging_cap:
    if user_logging_cap in usernames:
        print(f"Hello {user_logging.title()}, thank you for logging in again.")
    else:
        print('We need to find some users!')