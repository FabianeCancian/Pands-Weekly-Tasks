# https://docs.python.org/3/library/sys.html#sys.argv
# https://www.w3schools.com/python/ref_string_endswith.asp
# https://stackoverflow.com/questions/31689100/sys-argv1-indexerror-list-index-out-of-range


import sys
import os.path

# This function verify if the user entered the document name argument.
# The document name argument should be in sys.argv[1]
# If the user doesn't enter the file name,  the function will print an error message.
def readArgument():
    if (len(sys.argv) > 1):
        FILENAME = sys.argv[1]
        readFile(FILENAME)
    else:
        print ("Error paramenter not entered")

# This function will open the file and deal with possible errors.
def readFile(FILENAME):
# If the file is in the txt format the function will open the archive and count the e's.
    if str(FILENAME).endswith(".txt"):
        try:
            with open (FILENAME) as file:
                text = str (file.read())
                countE(text)
# If the file entered is in the txt format but it doesn't exist the function will return the message error.
        except IOError:
            if not os.path.isfile (FILENAME):
                print ("File does not exist")
            return 
# If the file entered is in other format than txt it will return the message error. 
    else:
        print("Format not supported")

# This funciton will count the amount of e's in the text.
# It starts with 0 and everytime that the letter in text is equal to E 1 is added to the count. 
def countE(text):
    count = 0
    for letter in text:
        if letter == 'e' or letter == 'E':
            count+=1
    print(f"This file contains {count} e's")

readArgument()

