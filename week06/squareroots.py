#https://realpython.com/python-lambda/
# https://mundoeducacao.uol.com.br/matematica/raiz-quadrada-aproximada.htm
# This link is in my native tongue, but it explain one way to calculate the approximate square root.
# By calculating the value from the nearest integer. 
# For example the square root of 20 is in between 4 and 5 (the square root of 16 and 25)

# This function find the nearest integer by multiplying i*i 
# Where i starts with the value 1 and it got increase by 1 when i*i is lower than the number entered
# Otherwise return the value of i 
# If the value entered is 20 it will return 5
def rearest_integer(number):
    i = 1
    calculation = 0
 
    while calculation <= number:
        calculation = i*i   
        if calculation >= number:
            return i
        else:
            i = i + 1
 
# This function receives the number entered by the user and the integer for the guess
# It will add 0.0000001 to guess while guess*guess is lower than the number
def find_approximation(number, guess):
    while guess*guess < number:
        guess = guess + 0.0000001
    return guess

# This function ask the user to enter a number
# Then, call rearest_integer() to find the nearest integer
# After that, call find_approximation() with the guess - 1 because guess is the nearest higher integer
# So, if the value guess is 5, we know that the root of 20 is between 4 and 5.
def sqrt():
    number = float(input("Enter a number:"))
    guess = rearest_integer(number)
    print(find_approximation(number, guess - 1))
          
sqrt()