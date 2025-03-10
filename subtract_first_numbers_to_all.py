#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []
for i in range(0,10):
    x = float(input(f'Enter number {i + 1}: '))
    numbers.append(x)
first = numbers[0]
x = 0
for a in range(0,9):
    print(f'{first} - {numbers[1+x]} = {first - numbers[1+x]}')
    x += 1