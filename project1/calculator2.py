def calculate():
    operation = input(''' 
Hello and welcome to Ginos 5 number calcualtor. For multiplication and divison please keep the numbers to 2 numbers and enter 0 for the rest, for addition and subtraction if you do not need all 5 numbers enter 0
Please type in the operation you would like to compute: addition, subtraction, multiplication, or division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    number_3 = int(input('Please enter the third number: '))
    number_4 = int(input('Please enter the fourth number: '))
    number_5 = int(input('Please enter the fifth number: '))



    if operation == 'addition':
        print('{} + {} + {} + {} + {} = '.format(number_1, number_2, number_3, number_4, number_5))
        print(number_1 + number_2 + number_3 + number_4 + number_5)

    elif operation == 'subtraction':
        print('{} - {} - {} - {} - {} = '.format(number_1, number_2, number_3, number_4, number_5))
        print(number_1 - number_2 - number_3 - number_4 - number_5)

    elif operation == 'multiplication':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == 'division':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Please eneter a valid operator.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Thank for using Ginos python calculator.')
    else:
        again()

calculate()
