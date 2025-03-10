#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))
try:
    quo = num_1 % num_2
    print(f'The quotient of the two numbers is {quo:.0f}')
except ZeroDivisionError:
    print('Can\'t print to 0')