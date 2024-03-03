#Ask the user for insert a number
number = int(input("Enter a number:"))
# print the value the user typed 
print (number)
# Check if the number is different than 1
while number != 1:
    # if it is different check if it is an even number.
    if (number % 2) == 0:
        #if even number divide by 2
        number = number/2
    #if odd number multiply by 3 and add one.
    else:
        number = (number*3) + 1
    # print the new number
    print(int(number))
#The system repeats the loop until the result is 1.