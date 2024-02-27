#Ask the user for insert account number
number = int(input('Please enter your account:'))
#Transforming number in string to be able to use the string function slicing
#https://www.w3schools.com/python/python_strings_slicing.asp
account = str(number)
#Print xxxxxx + last four digits.
print("xxxxxx{}".format(account[6:10]))