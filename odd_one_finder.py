#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd = []
for i in range(0,10):
    num = float(input(f'Enter number {i + 1}: '))
    if num % 2 != 0:
        odd.append(num)
    else:
        None
print(len(odd))