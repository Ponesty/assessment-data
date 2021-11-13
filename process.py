log_file = open("um-server-01.txt") #Opens a file object to be used in code


def sales_reports(log_file): #Creating a function called 'sales_reports'.
    for line in log_file: #Going through file line by line.
        line = line.rstrip() #Removing whitespaces at end of line
        day = line[0:3] #Day is equal to the first 3 lines in the file
        if day == "Mon": #checks if day is equal to 'Tue' is true.
            print(line) # Prints the lines with 'Tue' in it.


sales_reports(log_file) #Calls the sales_reports function with the open file and an argument.
