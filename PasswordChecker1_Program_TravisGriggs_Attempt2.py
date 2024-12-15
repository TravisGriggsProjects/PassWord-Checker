#Travis Griggs 5/03/2024 assignment PasswordChecker1

#pseudocode
#PROGRAM_PASSWORD_CHECKER
#PRINT HEADING
#
#MIN_PASSWORD_LENGTH = 6
#MAX_PASSWORD_LENGTH = 10
#
#INPUT PASSWORD
#
#Calculate password_length
#
#WHILE length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH::
#   Output an error message
#   Input password
#   Calculate password_length
#
#   Endwhile
#
#Output PASSWORD_LENGTH
#
#If Password is numeric then
#   COMMENT = "PASSWORD WEAK - only contains numbers"
#ELSE if Password is alphabetic then
#   COMMENT = "PASSWORD WEAK - only contains letters"
#ELSE
#   COMMENT = "PASSWORD STRONG"

#The following code defining the minimum and maximum length of an input password.
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

print("Assessment 2 - PasswordChecker part 1 by Travis Griggs")
#The input function allows for a user to input their own data. In this case the input required form the user is a password.
password = input("Please enter your password: ")
#The len function returns the number of charaters in a string, thus enabling the password length to be validated
password_length = len(password)

# The following while loop catches all invalid passwords, asks the user to re-input a password.
while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
    print("Invalid password length. Password must be between 6 and 10 characters.")
    password = input("Please enter your password: ")
    password_length = len(password)

print("Password length:", password_length)

    #The following if/elif statements check the input password against each of the conditions in sequential order. If the password is determined to contain both letters and numbers (i.e. the first two if statements are flase) then the password is deemed strong.
if password.isnumeric():
    print("Password weak - only contains numbers")
elif password.isalpha():
    print("Password weak - only contains letters")
else:
    print("Password strong - contains a combination of letters and numbers")