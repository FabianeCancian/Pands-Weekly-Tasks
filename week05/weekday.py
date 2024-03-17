# https://www.w3schools.com/python/python_datetime.asp
# This code pulls out what day it is today.
import datetime
x = datetime.datetime.now()
today = (x.strftime("%A"))
#I created a list with the days of the week and named it weekday
weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#I created a sublist with saturday and sunday (weekend) by pullin the itens 5 and 6 of the weekday list.
weekend = weekday [5:]

#https://www.w3schools.com/python/python_lists_access.asp
#creeated a condition where if today (for ex. Sunday) is in the lisk weekend the system will print message A, if today it is not in the weekend list the system will print message B.
if today in weekend:
    print("It is the weekend, yay!") 
else: print("Yes, unfortunately today is a weekday.")