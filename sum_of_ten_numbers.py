#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
numbers = []
for i in range(0,10):
    num = float(input(f'Enter number {i + 1}: '))
    numbers.append(num)
print(sum(numbers))