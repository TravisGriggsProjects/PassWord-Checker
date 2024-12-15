# Pseudocode
# def main
#   define counts variables (i.e. count_pw_too_small & count_pw_too_large) initially set to zero
#   list_data []
#   OPEN "ITWorks_password_log.txt" FOR INPUT AS input_file
#       FOR EACH line IN input_file
#           APPEND line to list_data
#       ENDFOR
#
#   CLOSE input_file
#
#   FOR error IN list_data
#       OUTPUT error
#
#       if index has a "password < 6" in it (i.e. the password is too small) then increase count_pw_too_small by 1
#
#       elif index has a "password >10 " in it (i.e. the password is too large) then increase count_pw_too_large by 1
#
#   ENDFOR
#
#   OUTPUT Count of passwords too short & Count of passwords too long
#
# END


def main():
    #The code below sets the inital count of both types of errors to zero
    count_pw_too_small = 0
    count_pw_too_large = 0

    #Defining a list with empty square brackets creates an empty list, for which Indexes may  be latter appended to.
    list_data = []

    #The follwoing code opens "ITWorks_password_log.txt" as a read only file, as we don't want to override or change anything in the file.
    input_file = open("ITWorks_password_log.txt", "r")

    #The following code appends each line in the opened file to our previously created list.
    for line in input_file:
        list_data.append(line)

    #As we are done with the file we close it, as below:
    input_file.close()

    for error in list_data:
        print(error, end="")

        #password < 6 was chosen as the search term as it is spefici enough to ensure only the errors in the list sited for being to small are counted.
        if "password < 6" in error:
            count_pw_too_small += 1

        elif "password > 10" in error:
           count_pw_too_large += 1

    #The following code outputs the final counts of each type of error
    print("Count of passwords too short:", count_pw_too_small)
    print("Count of passwords too long:", count_pw_too_large)

main()