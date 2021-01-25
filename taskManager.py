# Define function
def reg_user():

    # Open file
    f2 = open('user.txt','a')
    # Request user input
    username_new = input("Please enter new username:    ")
    
    # Create a while to constantly request a new username if the user enters a username that already exists
    while username_new in usernames:
        
        # Display statement
        # Then request user input again
        print("Username already exists!")
        username_new = input("Please enter new username:    ")

    # Request user input
    password_new = input("Please enter new password:    ")
    password_confirm = input("Please confirm new password by entering it again: ")


    # Create a while loop
    # This loop confirms the new password by checking if the new password is the same as the confirmed password
    # This loop will run whilst the new password is not the same as the confirmed password
    while password_new != password_confirm:
        print("Incorrect password.")
        password_confirm = input("Please confirm new password by entering it again: ")

    # If the new passwrod matches the confirmed password then it will write the new password and the new username to the file
    if password_new == password_confirm:
            f2.write("\n" + username_new + ", " + password_new)

# Define function
def add_task():

    # Open file
    f1 = open('tasks.txt','a')
    
    # Request user input
    worker_name = input("Please enter the username of the person the task is assigned to:   ")
    task_title = input("Please enter the title of the task:    ")
    task_descrip = input("Please enter the discription of the task:    ")
    year = int(input("Please enter the year it is due on e.g. 2011, 2019 :    "))
    month = int(input("Please enter the month it is due e.g. o4, 12 , 09 etc :    "))
    day = int(input("Please enter the day it is due e.g. 02, 20 :    "))
    
    # Initialise variable to store the due date
    due_date = datetime.datetime(year, month, day)
    
    # Format the due date to a string data type
    due_date = due_date.strftime("%Y-%m-%d")

    # Get the current date
    date_assigned = datetime.datetime.now()
    completeness = "No"

    # Create new variable to store user inputs
    new_task = (f'\n{worker_name}, {task_title}, {task_descrip}, {date_assigned}, {due_date}, {completeness}')
    
    # Write the variable to the file
    f1.write(new_task)

# Define function
def view_all():

     
    # Open file to read from it
    f1 = open('tasks.txt','r')

    # Initialise the variable to 1
    dict_count_2 = 1

# Create a for loop to iterate through the file
    for a in f1:
        
        # Replace the newline character with an empty charcater for every line in the file
        a_replaced = a.replace("\n","")

        # Split the line into a list whenever it comes across a comma "," and an empty space " "
        a_split = a_replaced.split(", ")
        
        # Print the task number
        print("Task Number:    "+ str(dict_count_2))

        # Print the username the task is assigned to
        print("Assigned to:    " + a_split[0])

        # Print the title of the task 
        print("Title:    " + a_split[1])

        # Print the task discription
        print("Task description:    " + a_split[2])

        # Print the date assigned
        print("Date given:    " + a_split[3])

        # Print the due date
        print("Due date:    " + a_split[4])

        # Print whether the task is complete or not
        print("Task complete ?:    " + a_split[5] + "\n")  

        # Increment "dict_count_2" by 1 after every iteration
        dict_count_2 += 1
    
    # Close the file
    f1.close()

# Define function
def view_mine():

    # Open the file for reading only
    f1 = open('tasks.txt','r')

    # Create an empty dictionary to all the tasks with their own keys and values
    tasks_dic = {}

    # Initialise "dict_count" to 1
    dict_count = 1
    # Create a for loop
    # This for loop will read the file sentence for sentence or rather line for line
    for line in f1:
        
        # Replace the newline character with an empty string
        lines = line.replace("\n","")

        # Split the lines in the file
        task = lines.split(", ")

        # Use the below line to
        # Store each task with its unique task number so it can be stored in the dictionary in a key value format
        tasks_dic[dict_count] = task
        
        # If the first word in the sentence is the same as the username entered
        # Then it will print that sentence
        if task[0] == username:
            
            # Print the task number
            print("Task Number:    "+ str(dict_count))

            # Print the task title
            print("Title:    " + task[1])

            # Print the task description
            print("Task description:    " + task[2])

            # Print the date assigned
            print("Date given:    " + task[3])

            # Print the due date
            print("Due date:    " + task[4])

            # Print whether the task is complete or not
            print("Task complete ?:    " + task[5] + "\n")  

        # Increment "dict_count" by 1 after every iteration
        dict_count += 1
    
    # Close the file
    f1.close()

    # Display newline characters to make the output more user friendly
    print("\n" + "\n")

    # Request user input
    task_select = int(input("Please enter the task number of the task you want to select or enter \"-1\" to return to the main menu:    "))
    
    # Create a while loop to continuosly run while the user input "task_select" is not -1
    while task_select != -1:
        
        # Initialise variable "selected" to the dictionary key selected by the user in "task_select"
        task_selected = tasks_dic[task_select]

        # Print the selected task "value of the key selected by user"
        print(task_selected)
    
        # Request user input    
        task_completeness = input("Please enter \"c\" to mark as complete or enter \"e\" to edit the task:    ")


        # If user input is "c"
        if task_completeness == "c":
            
            # Then change the last character of the task to yes
            task_selected[-1] = "yes"

        # Or if the user input is "e" and the last character of the task is already yes
        elif task_completeness == "e":

            if task_selected[-1] != "yes":

                # Request user input
                edit = input("Enter \"u\" to edit the username or enter \"d\" to edit the due date:    ")
                
                # If user input is "u"
                if edit == "u":

                    # Then request user input 
                    task_selected[0] = input("Please enter the new username:    ")
                
                # Or if the user input is "d"
                elif edit == "d":

                    # Then request user input
                    year = int(input("Please enter the year it is due on e.g. 2011, 2019 :    "))
                    month = int(input("Please enter the month it is due e.g. o4, 12 , 09 etc :    "))
                    day = int(input("Please enter the day it is due e.g. 02, 20 :    "))

                    # Initialise variable to store the due date
                    due_date = datetime.datetime(year, month, day)

                    # Format the due date to a string data type
                    due_date = due_date.strftime("%Y-%m-%d")
                    
                    # Update the due date
                    task_selected[-2] = due_date
            else:
                print('Task is already completed')
        
            # Or else display the error message
        else:
            print("You have entered an invalid option!")

        # Request user input
        task_select = int(input("Please enter the task number of another task you want to select or enter \"-1\" to return to the main menu:    "))
    
    # writting to the file
    f1 = open('tasks.txt','w')
    
    # Creating an empty string variable
    Alltaskdata = ''

    # Create a for loop to iterate through the file
    for tasklist in tasks_dic.values():

        # Join the list using a comma "," and a space " "
        Alltaskdata += ', '.join(tasklist) + '\n'

    # Remove only the last newline character
    Alltaskdata = Alltaskdata.strip('\n')

    # Write to the file
    f1.write(Alltaskdata)
        
    

# Define function
def task_overview():

    # Open files
    f1 = open('tasks.txt','r')
    f3 = open('task_overview.txt','w')

    # Initialise the counting variables to 0
    count_line_1 = 0
    count_line_2 = 0
    count_line_3 = 0
    count_line_8 = 0
    count_line_9 = 0
    
    # Create for loop to iterate through file
    for line in f1:

        # Increment counting variable by 1 for every iteration
        count_line_1 += 1

        # Remove the newline characters in every line
        lines_2 = line.strip("\n")

        # Split the the line into a list where there is a (", ")
        lines_seperated = lines_2.split(", ")

        # If the final character for the line is "yes"
        if lines_seperated[-1] == "yes":
            
            # Then increment the counting variable by 1 after every iteration
            count_line_2 += 1
            
        # Or if the final character is not "yes"
        else:

            # Then increment the counting variable by 1
            count_line_3 += 1

        # If the final character for the line is "No" and the date assigned is greater than due date 
        if lines_seperated[-1] == "No" and lines_seperated[-3] > lines_seperated[-2]:

        # Then increment the counting variable by 1
            count_line_8 += 1

        # If the date assigned is greater than the due date
        if lines_seperated[-3] > lines_seperated[-2]:
            
            # Then increment the counting variable by 1
            count_line_9 += 1

    # Calculate the percentage of incomplete tasks
    incomp_percentage = (count_line_3 / count_line_1) * 100

    # Calculate the percentage of overdue tasks
    overdue_percentage = (count_line_9 / count_line_1) * 100

    # Write to the files
    f3.write(f'The total number of tasks is {count_line_1}\n\n')
    f3.write(f'The total number of completed tasks is {count_line_2}\n\n')
    f3.write(f'The total number of incomplete tasks is {count_line_3}\n\n')
    f3.write(f'The total number of tasks that haven\'t been completed and are overdue is {count_line_8}\n\n')
    f3.write(f'The percentage of tasks that are incomplete is {incomp_percentage} %\n\n')
    f3.write(f'The percentage of tasks that are overdue is {overdue_percentage} %')
    
    # Close the files
    f1.close()
    f3.close()

    # Returning number of tasks
    return count_line_1

# Define the function to take in the username and total task number
def each_user(us_name, tot_task_num):

    # Open the file for reading
    f1 = open('tasks.txt','r')

    # Initialise the counting variables to 0
    count_line_5 = 0
    count_line_6 = 0
    count_line_7 = 0
    count_line_10 = 0
    user_total_task_complete = 0
    user_total_task_percent = 0

    # Create for loop to iterate through file
    for lines in f1:

        # Remove the newline character at the end of the line
        lines_strip = lines.strip("\n")

        # Split the line into a list at these points (", ") in the line
        lines_split = lines_strip.split(", ")
        
        # If the the first character in the list is equal to the username
        if lines_split[0] == us_name:
          
            # Then increment the counting variable by 1
            count_line_5 += 1

            # Calculate the percentage of the total number of tasks assigned to the user
            user_total_task_percent = (count_line_5 / tot_task_num) * 100
            
            # If the final character in the line is "yes"
            if lines_split[-1] == "yes":

                # Then increment the counting variable by 1
                count_line_6 += 1
            
            # Or if the final character in the line is not "yes"
            else:

                # Then increment the counting variable by 1
                count_line_7 += 1
                    
            # If the last character of the line is "No" and the date assigned is greater than the due date
            if lines_split[-1] == "No" and lines_split[-3] > lines_split[-2]:
                
                # Then increment the counting variable by 1
                count_line_10 += 1
    
    # Initialise the variables to 0
    user_total_task_complete = 0
    user_total_task_incomplete = 0
    user_total_task_overdue_percentage = 0
    
    # If the counting variable is greater than 0
    if count_line_5 > 0:

        # Then calculate the answers
        user_total_task_complete = (count_line_6 / count_line_5) * 100
        user_total_task_incomplete = (count_line_7 / count_line_5) * 100
        user_total_task_overdue_percentage = (count_line_10 / count_line_5) * 100
    
    # Close the file
    f1.close()

    # Return the following statement
    return f'''The total number of tasks for {us_name} is {count_line_5}\n
    The percentage of the total number of tasks assigned to the user is {user_total_task_percent} %\n
    The percentage of tasks assigned to the user that are complete is {user_total_task_complete} %\n
    The percentage of tasks assigned to the user that must still be completed is {user_total_task_incomplete} %\n
    The percentage of tasks assigned to the user that have not yet been completed and are overdue is {user_total_task_overdue_percentage} %'''

# Define the function
def user_overview():

    # Open files
    f2 = open('user.txt','r')
    f4 = open('user_overview.txt','w')
    
    # Initialise the function to a variable
    tot_task_num = task_overview()
    
    # Initialise the counting variable to 0
    count_line_4 = 0

    # Create a for loop to iterate through the file
    for line in f2:

        # Increment the counting variable by 1
        count_line_4 += 1

    # Write the following statements to the file
    f4.write(f'The total number of users is {count_line_4}\n\n')
    f4.write(f'The total number of tasks is {tot_task_num}\n\n\n')
    
    # Initialise the variable to an empty string variable
    tofile = ""

    # Create a for loop to iterate through the list
    for us in usernames:

        # Display statement showing the username  and many equals signs that form a line "The line is to make the output more user friendly"
        tofile +="for user: "+ us +"\n===================================\n"

        # Add each user and the total number of tasks to the empty string "tofile"
        tofile += each_user( us,tot_task_num)

        # Print many equals signs that form a line "The line is to make the output more user friendly"
        tofile +="\n=======================================================================================================\n"
    
    # Remove the newline character at the end of the string in the variable
    tofile = tofile.strip('\n')

    # Write the variable to the file
    f4.write(tofile)
 
# Define function 
def gen_report():

    # Call 2 other functions    
    task_overview()
    user_overview()

# Define the function
def disp_stats():
    
    # Call function to generate files
    gen_report()

    # Open the generated files
    f3 = open('task_overview.txt','r')
    f4 = open('user_overview.txt','r')


    # Store the files in variables
    tasks_info = f3.read()
    user_info = f4.read()

    # Display the variables
    print(f'Task information:\n\n{tasks_info}\n\n\nUser information:\n\n{user_info}')

    # Close the files
    f3.close()
    f4.close()
    
# Import date to use current date
# Import sys to be able to use "exit" to exit program

import datetime
import sys

# Open files 
# Open file "tasks.txt" with "a" to be be able to add data to it
# Open file "user.txt" with "r+" to be able to read and write to file
f2 = open('user.txt','r+')

# Create lists "usernames" and "passwords" to store all the usernames and all the passwords in them
usernames = []
passwords = []

# Use "date.today" to get the current date
today = datetime.date.today()

# Request user input
username  = input("Please enter your username:    ")

# Create loop to loop through the file
for contents in f2:
    contents = contents.replace("\n","")  # Use .replace to remove the newline characters in the file
    conts = contents.split(", ")  # Use split to split the file into a list
    usernames.append(conts[0])  # Use .append to continuously add usernames to usernames list 
    passwords.append(conts[1])  # Use .append to continuosly add passwords to passwords list

# Close the file           
f2.close()
# Create a while loop to iterate though usernames list
# This loop will only execute if the username entered by the user is wrong
while not username in usernames:
    print("Wrong  username !")
    username = input("Please enter your username:  ")
    
# initialise position to 0
position = 0

# Create a for loop to iterate through username list
# This loop will only execute if the user enters a valid username
for u in usernames:
    if u ==  username:  # If the username entered by user is the same as the username currently being checked by "u" then we stop iterating through usernames list
        
        # Use break to exit loop
        break
    position += 1   # If the username entered by user is not the same as the username currently being checked by "u" then we increment "position" by 1 then check the next username in the list

# Request user input
password = input("Enter password:   ")

# Create a while loop
# This while loop will continuously execute if the password entered is not in the same position in the list as the username entered. Meaning they do not match
while password != passwords[position]:
     print("Wrong password!")
     password = input("Please enter the correct password:   ")

# Create an empty string variable to intialise th menu option
menu_opt = ''

# Create loop to continue running until the menu option is "e"
while menu_opt != "e":

    # If the username entered is "admin" then it will display this menu option
    if username == "admin":
        
        # Request user input
        menu_opt = input('''Please select one of the following options:
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit\n:    ''')

    # If the username entered is not "admin" but still a valid username then it will display this menu option
    else:
        menu_opt = input('''Please select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit\n:    ''')



    # If user input is "r"
    if menu_opt == "r":

        # Call function
        reg_user() 
    

    # If user input is "a"
    elif menu_opt == "a":
    
        # Call function
        add_task()
   
    # If user inputs "va"
    elif menu_opt == "va":
    
        # Call function
        view_all()

    # If user enters "vm"
    elif menu_opt == "vm":

        # Call function
        view_mine()

    # If the user input is "gr"
    elif menu_opt == "gr":
    
        # Call function
        gen_report()

    # If user input is "ds"
    elif menu_opt == "ds":

        # Call function
        disp_stats()

# Close file
f2.close()