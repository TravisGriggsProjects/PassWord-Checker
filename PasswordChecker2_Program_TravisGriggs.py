#Travis Griggs 10/03/2024 assignment PasswordChecker2

import datetime
def main():
    print("Assessment 2 - PasswordChecker part 2 by Travis Griggs")

    #The following code defining the minimum and maximum length of an input password.
    MIN_PASSWORD_LENGTH = 6
    MAX_PASSWORD_LENGTH = 10

    #The following code creates the variable message, and sets it initially to nothing
    message = ""

    #The following code opens the password_log file and allows for data to be appended to it.
    log_file = open('password_log_Travis_Griggs.txt', "a")

    #The input function allows for a user to input their own data. In this case the input required form the user is a password.
    password = input("Please enter your password: ")
    #The len function returns the number of characters in a string, thus enabling the password length to be validated
    password_length = len(password)

    #The following while loop catches all invalid passwords, stores the reason as to why is was deemed invalid, the current date time at which the invalid password was entered, and finally asks the user to re-input a password.
    while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:

        print("Invalid password length. Password must be between 6 and 10 characters.")
        current_date_and_time = datetime.datetime.now()
        if password_length < MIN_PASSWORD_LENGTH:
            #The following code defines the reason the password was invalid, as well as the message to be outputted to the log file.
            reason_password_invalid = "password < 6"
            message = f"{current_date_and_time} - {reason_password_invalid}\n"

        elif password_length > MAX_PASSWORD_LENGTH:
            reason_password_invalid = "password > 10"
            message = f"{current_date_and_time} - {reason_password_invalid}\n"

        #The following code writes the message defined in the if statements to the log_file and subsuequently asks for the user to re-input a password, as the previous one was invalid.
        log_file.write(message)
        password = input("Please enter your password: ")
        #The len function returns the number of characters in a string, thus enabling the password length to be rechecked. If the length is still invalid (i.e. it lies outside of the range >=6 <=10) the while loop is repeated, otherwise the program will continue onwards.
        password_length = len(password)

    #As we are done with the file we close it, as below:
    log_file.close()

    print("Password length:", password_length)

    #The isnumeric() function returns True if all the characters are numeric (0-9), thus allowing us to determine if the password only contains numbers.
    if password.isnumeric():
        print("Password weak - only contains numbers")
    #The isalpha() function returns True if all the characters are alphabet letters (a-z), thus informing us if passwrod only contains letters.
    elif password.isalpha():
        print("Password weak - only contains letters")
    else:
        print("Password strong - contains a combination of letters and numbers")

    # The following code opens the password_log file as a read only file. This is choosen as we don't want to change any information in the file only view it as it is.
    log_file = open('password_log_Travis_Griggs.txt', "r")

    for line in log_file:
        print(line, end='')
        #This for loop reads each line in the log file and outputs them to the screen.

    # As we are done with the file we close it, as below:
    log_file.close()

main()