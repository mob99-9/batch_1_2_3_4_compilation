#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
numbers = []
for i in range(0,10):
    num = float(input(f'Enter number {i + 1}: '))
    if num % 2 == 0:
        numbers.append(num)
    else:
        None
    i += 1
print(numbers)
print(f'\nThere are {len(numbers)} even numbers')