###################
# Midterm-project: 
###################

from collections import Counter
import datetime

#########
# Admin:
#########

def displayAdminMenu():
    print("Admin menu:")
    print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")

def displayStatistics(matrix):
    # Worst case: O(N)
    event_list = []
    # Displaying the most common event in a matrix of tickets and events.
    for row in range(len(matrix)):
        event_list.append(matrix[row][1])
    event_list = Counter(event_list)
    return event_list.most_common(1)[0][0]# Got this method by researching on google(geeksforgeeks). It gives you the most frequent element in a list.

def adminBookTicket(username, event_id, date_of_event, priority):
    tickets_file = open("tickets.txt", "a")# a for appending in order to insert after the last line.
    # autoincrementing the ticket id and then writing the ticket values into the file
    tick_id = incrementTicketId()
    tickets_file.write("\n" + tick_id + ", " + event_id + ", " + username + ", " + date_of_event + ", " + str(priority))
    tickets_file.close()

def displayAllTickets():
    # Worst case: O(N)
    # today's date
    td_date = datetime.datetime.now()
    td_date = td_date.strftime("%Y%m%d")# Got this method by researching on google(https://www.w3schools.com/python/python_datetime.asp).
    tickets_matrix = importTickets()
    date_matrix = []
    for row in range(len(tickets_matrix)):
        # Casting the dates into an integer and then comparing them in order to be able to compare them.
        # Appending the date matrix with all the dates that are >= to today's date.
        if(int(tickets_matrix[row][3]) >= int(td_date)):
            date_matrix.append(tickets_matrix[row])
    # returning the date matrix to display (today, tomorrow, and onward's tickets and event ids')
    return date_matrix

def changeTicketPriority(ticket_id, priority):
    # Worst case: O(N)
    tickets_matrix = importTickets()
    boolean = True
    # changing the priority of a ticket by providing it's id
    for row in range(len(tickets_matrix)):
        if(ticket_id == tickets_matrix[row][0]):
            tickets_matrix[row][4] = priority
            return tickets_matrix[row]
        else:
            boolean = False
    if not boolean:
        return False

def disableTicket(ticket_id):
    # Worst case: O(N)
    tickets_matrix = importTickets()
    boolean = True
    # removing the ticket by providing it's id
    for row in range(len(tickets_matrix)):
        if(ticket_id == tickets_matrix[row][0]):
            tickets_matrix.remove(tickets_matrix[row])
            return tickets_matrix
        else:
            boolean = False
    if not boolean:
        return False

def runEvents():
    # Worst case: O(N + N + N ^ 2) 
    td_date = datetime.datetime.now()
    td_date = td_date.strftime("%Y%m%d")
    tickets_matrix = importTickets()
    td_events = []
    temp_matrix = tickets_matrix[:]
    # Appending todays evenst to a new matrix
    for row in range(len(tickets_matrix)):# O(N)
        if(int(tickets_matrix[row][3]) == int(td_date)):
            td_events.append(tickets_matrix[row])
    # Removing today's events from the tickets matrix
    for row in range(len(tickets_matrix)):# O(N)
        if(int(tickets_matrix[row][3]) == int(td_date)):
            temp_matrix.remove(tickets_matrix[row])
    # returning the sorted matrix for today's event
    # And the sorting is being done according to index 4 of the matrix which is the priority index
    return selectionSort(td_events, 4)# O(N ^ 2)

########
# User:
########

def displayUserMenu():
    print("User menu:")
    print("1. Book a ticket\n2. Exit")

def bookTicket(username, event_id, date_of_event):
    tickets_file = open("tickets.txt", "a")
    def_priority = 0
    tick_id = incrementTicketId()
    tickets_file.write("\n" + tick_id + ", " + event_id + ", " + username + ", " + date_of_event + ", " + str(def_priority))
    tickets_file.close()

##################
# Common methods:
##################

def importTickets():
    # Worst case: O(N + N)
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
    for line in tickets_file: # Worst case: O(N) n number of lines
        tickets.append(line.strip("\n"))
    for row in range(num_lines): # Worst case: O(N) n rows
        tickets_matrix.append(tickets[row].split(","))
    return tickets_matrix

def incrementTicketId(): # this method is for autoincrementing the ticket id
    # Worst case: O(N)
    tickets_matrix = importTickets()
    tickets_id = []
    for row in range(len(tickets_matrix)):
        tickets_id.append(tickets_matrix[row][0])
    last_id = tickets_id[len(tickets_id) - 1]
    temp_id = last_id[4:]
    temp_id = int(temp_id) + 1
    tick_id = "tick" + str(temp_id)
    return tick_id

def selectionSort(matrix, i):
    # worst case: O(N^2)
    # Selection sort for a matrix with a specific index
    for row in range(len(matrix) - 1):
        for row2 in range(row + 1, len(matrix)):
            if(matrix[row][i] > matrix[row2][i]):
                temp = matrix[row]
                matrix[row] = matrix[row2]
                matrix[row2] = temp
    return matrix

########
# Main:
########

def main():
    # Importing tickets from the text file into a matrix
    tickets_matrix = importTickets()
    #print(tickets_matrix)
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
                event_id = input("Please insert the event ID for the ticket: ")
                date_of_event = input("Please insert the date of the event in the following format(YYYYMMDD): ")
                bookTicket(username, event_id, date_of_event)
            else:
                print("Wrong choice please choose one of the below choices: ")
            print()
            choice = eval(input("Please choose a number: "))
    else: # choosing from admin menu
        while(choice != 7):
            if(choice == 1):
                print()
                print("The event ID with the highest number of tickets is:", displayStatistics(tickets_matrix))
                print()
            elif(choice == 2):
                print("Booking a ticket for an event:")
                print()
                name = input("Please specify the name of the ticket holder: ")
                event_id = input("Please insert the event ID for the ticket: ")
                date_of_event = input("Please insert the date of the event in the following format(YYYYMMDD): ")
                priority = int(input("Please specify the priority of your ticket: "))
                adminBookTicket(name, event_id, date_of_event, priority)
                print()
                # Here if the admin wants to continue booking tickets he can without returning to the menu page.
                continue_booking = input("Would you like to book another ticket yes/no?: ")
                if(continue_booking == "yes" or continue_booking == "no"):
                    while(continue_booking == "yes"):
                        print()
                        print("Booking a ticket for an event:")
                        print()
                        name = input("Please specify the name of the ticket holder: ")
                        event_id = input("Please insert the event ID for the ticket: ")
                        date_of_event = input("Please insert the date of the event in the following format(YYYYMMDD): ")
                        priority = int(input("Please specify the priority of your ticket: "))
                        adminBookTicket(name, event_id, date_of_event, priority)
                        print()
                        continue_booking = input("Would you like to book another ticket yes/no?: ")
                        print()
                else:
                    print("Incorrect input.")
                    print("Back to admin menu:")
                    print()
            elif(choice == 3):
                print("Displaying new tickets with today's date and future dates.")
                print("Old tickets are not shown.")
                print(displayAllTickets())
            elif(choice == 4):
                ticket_id = input("Please specify the ticket id in which you wish to change it's priority: ")
                priority = input("Please insert the ticket's new priority: ")
                if(changeTicketPriority(ticket_id, priority) == False):
                    print("The ticket id was not found.")
                else:
                    print(changeTicketPriority(ticket_id, priority))
            elif(choice == 5):
                ticket_id = input("Please specify the ticket id in which you wish to remove from the system: ")
                if(disableTicket(ticket_id) == False):
                    print("The ticket id was not found.")
                else:
                    print("The ticket with ID:", ticket_id, "was successfully removed from the system. ")
                    print(disableTicket(ticket_id))
            elif(choice == 6):
                print(runEvents())
            else:
                print("Wrong choice please choose one of the below choices: ")
            print()
            choice = eval(input("Please choose a number: "))
main()