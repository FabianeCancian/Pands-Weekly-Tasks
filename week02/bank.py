#Ask the user for the first amount
amount1 = int(input('Enter amount1(in cent):'))
#Ask the user for the second amount
amount2 = int(input('Enter amount2(in cent):'))
#the result is the sum of 2 amounts and then divided by 100, this means the conversion of cents to euro
result = (amount2 + amount1)/100
#now I print the result
#I used the solution .2f after the result to show 2 decimals
print (f'The sum of {amount1}c and {amount2}c is €{result:.2f}')
