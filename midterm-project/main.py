###################
# Midterm-project: 
###################

from collections import Counter

#########
# Admin:
#########

def displayAdminMenu():
    print("Admin menu:")
    print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")

def displayStatistics(matrix):
    event_list = []
    for row in range(len(matrix)):
        event_list.append(matrix[row][1])
    event_list = Counter(event_list)
    return event_list.most_common(1)[0][0]# Got this method by researching on google. It gives you the most frequent element in a list.

def adminBookTicket():
    print("i am in admin ticket booking")

def displayAllTickets():
    print("i am in admin display tickets")

def changeTicketPriority():
    print("i am in admin change ticket priority")

def disableTicket():
    print("i am in admin disable ticket")

def runEvents():
    print("i am in admin run events")

########
# User:
########

def displayUserMenu():
    print("User menu:")
    print("1. Book a ticket\n2. Exit")

def bookTicket():
    print("i am in ticket booking")

##################
# Common methods:
##################

def importTickets():
    # Opening the file and reading number of lines
    tickets = []
    tickets_matrix = []
    tickets_file = open("tickets.txt", "r")
    num_lines = len(tickets_file.readlines())
    tickets_file.close()
    # Opening the file and reading the content of the lines
    # appending the content into a list
    # then changing the list into a matrix of tickets
    tickets_file = open("tickets.txt", "r")
    for line in tickets_file:
        tickets.append(line.strip("\n"))

    for row in range(num_lines):
        tickets_matrix.append(tickets[row].split(","))
    return tickets_matrix

########
# Main:
########

def main():
    # Importing tickets from the text file into a matrix
    tickets_matrix = importTickets()
    print(tickets_matrix)
    # Displaying user or admin menu
    print("Admin/Users login form:")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if(username != "admin" and password == ""): # user menu
        print()
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
                print()
                displayAdminMenu()
                attempts = 0
            attempts -= 1
    print()
    # Choosing from user/admin menu 
    choice = eval(input("Please choose a number: "))
    if(username != "admin"): # chosing from user menu
        while(choice != 2):
            if(choice == 1):
                bookTicket()
            else:
                print("Wrong choice please choose one of the below choices: ")
            choice = eval(input("Please choose a number: "))
    else: # choosing from admin menu
        while(choice != 7):
            if(choice == 1):
                print("The event ID with the highest number of tickets is:", displayStatistics(tickets_matrix))
            elif(choice == 2):
                bookTicket()
            elif(choice == 3):
                displayAllTickets()
            elif(choice == 4):
                changeTicketPriority()
            elif(choice == 5):
                disableTicket()
            elif(choice == 6):
                runEvents()
            else:
                print("Wrong choice please choose one of the below choices: ")
            choice = eval(input("Please choose a number: "))
main()