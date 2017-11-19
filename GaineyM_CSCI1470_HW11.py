###############################################################################
#
# Name: Michael Gainey
#
# Course: CSCI 1470
#
# Assignment: Homework #11
#
# Pseudocode:
#
#   Define a function copyFiles that doesn't take arguments:
#       Set filename1 to a user entered file name
#       Set filename2 to a user entered file name
#
#       Start a try block:
#           Open filename1 for reading and filename2 for writing using with
#               Set contents to the contents of filename1
#               Write contents to filename2
#
#       If an exception occured:
#           Print an error message
#
#
#   Define a function compareFiles that doesn't take arguments:
#       Set filename1 to a user entered file name
#       Set filename2 to a user entered file name
#
#       Start a try block:
#           Open filename1 and filename2 for reading using with
#               Start a while loop:
#                   Set file1line to the next line of filename1
#                   Set file2line to the next line of filename2
#
#                   If file1line and file2line differ:
#                       Print a message that the files differ
#                       Print file1line
#                       Print file2line
#                       Return to the main program loop
#
#                   If file1line and file2line are both empty strings:
#                       Print a message that the files are identical
#                       Return to the main program loop
#
#       If an exception occured:
#           Print an error message
#
#
#   Begin a while loop:
#       Print a message: "Choose an option below:"
#       Print "(1) Copy files"
#       Print "(2) Compare files
#       Print "(3) Stop
#
#       Set choice to the user's answer
#
#       If choice is '1' execute the copyFiles function
#       else, if choice is '2' execute the compareFiles function
#       else, if choice is '3' exit the loop
#
###############################################################################

def copyFiles():
    filename1 = input("Enter the name of a text file to copy FROM: ")
    filename2 = input("Enter the name of a text file to copy TO:   ")

    try:
        with open(filename1, 'r') as file1, open(filename2, 'w') as file2:
            contents = file1.read()
            file2.write(contents)
    except:
        print()
        print("File operation error!  Your file was not written.")


def compareFiles():
    filename1 = input("Enter the name of the first text file to compare:  ")
    filename2 = input("Enter the name of the second text file to compare: ")

    try:
        with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
            while True:
                file1line = file1.readline()
                file2line = file2.readline()

                if file1line != file2line:
                    print()
                    print("{} and {} are different starting in the following line: ".format(filename1, filename2))
                    print("  {}: {}".format(filename1, file1line[:-1])) # [:-1] removes the newline character
                    print("  {}: {}".format(filename2, file2line[:-1]))
                    return # the files are different -- exit the loop

                if file1line == '' and file2line == '':
                    # the end of both files has been reached with no differences
                    print()
                    print("{} and {} are identical!".format(filename1, filename2))
                    return # the end of the files has been reached -- exit the loop

    except:
        print()
        print("File operation error!  Your files were not compared.")


while True:
    print()
    print("Choose an option below:")
    print("(1) Copy files")
    print("(2) Compare files")
    print("(3) Stop")
    print()
    choice = input("Your choice (1-3): ")
    print()

    if choice == '1':
        copyFiles()
    elif choice == '2':
        compareFiles()
    elif choice == '3':
        break

    
# Homework #11

# Due: Tuesday, November 28th

# Write a program that provides the user with three options:
#      (1) Copy files 
#      (2) Compare files
#      (3) Stop

# For option (1), the program should prompt the user for the names of two text files.
# The content of the first file will be copied to the second file.

# For option (2), the program should prompt the user for the names of two text files and
# - determine if the contents of the two files are identical.
# - After the comparison, it should indicate whether or not they are identical.
# - If they are not identical, the program should display the first lines from each file that differ from each other.

# The program should terminate only when option (3) is chosen.
