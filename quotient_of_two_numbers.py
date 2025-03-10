#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
try:
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    quotient = num_1/num_2 
    print(f'{quotient:.2f}')
except ZeroDivisionError:
    print('Can\'t divide to zero')