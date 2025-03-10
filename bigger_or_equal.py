#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num_1 = int(float(input('Enter the first number: ')))
num_2 = int(float(input('Enter the second number: ')))
if num_1 < num_2:
    print(f'The bigger number is {num_2}')
elif num_1 > num_2:
    print(f'The bigger number is {num_1}')
else:
    print(f'Equal')