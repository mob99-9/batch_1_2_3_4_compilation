#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))
if num_1 != num_2:
     print(f'Not Equal ')
elif num_2 == num_1:
     print(f'Equal')
else:
     print(f'Invalid Inputs')