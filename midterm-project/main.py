###################
# Midterm-project: 
###################

#########
# Admin:
#########

def displayAdminMenu():
    print("Admin menu:")
    print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")

########
# User:
########

def displayUserMenu():
    print("User menu")
    print("1. Book a ticket\n2. Exit")
########
# Main:
########

def main():
    # Displaying user or admin menu
    print("Admin/Users login form:")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if(username != "admin" and password == ""): # user menu
        displayUserMenu()
    else: # admin menu
        attempts = 5
        while(attempts > 0):# loop over number of attempts
            if(username != "admin" or password != "admin123123"):
                print("Incorrect username and/or password, please try again.")
                print(attempts, " attempt/s left.")
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                if(username == "admin" and password == "admin123123"):
                    displayAdminMenu()
                    attempts = 0
            else:
                displayAdminMenu()
                attempts = 0
            attempts -= 1
    print("I AM HEREEEEE")
main()