# Define our function
def calculate():

	operation = input('''
Please tye in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for divison
''')

number_1 = int(input('Enter your first number here: '))
number_2 = int(input('Enter your second number here: '))

# Addition
if operation == '+':
	print('{} + {} = '.format(number_1, number_2))
	print(number_1 + number_2)

# Subtraction
elif operation == '-':
	print('{} - {} = '.format(number_1, number_2))
	print(number_1 - number_2)

# Multiplication
elif operation =='*':
	print('{} * {} = '.format(number_1, number_2))
	print(number_1 * number_2)

# Division
elif operation =='/':
	print('{} / {} = '.format(number_1, number_2))
	print(number_1 / number_2)

else:
	print('You have nt typed a valid operator, please run the program again.')

# Add again() function to the calculate() function
again()

def again():
	calc_again = input('''
do you want to calculate again?
please type y for yes and n for no
''')

if calc_again.upper() == 'y':
	calculate()
elif calc_again.upper =='n':
	print('Goodbye')
else:
	again()
calculate()

