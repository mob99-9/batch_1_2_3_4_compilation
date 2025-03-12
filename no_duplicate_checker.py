#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#create lists
numbers = []
no_duplicates = []

#ask for 10 numbers
for num in range(0,10):
    ask_num = float(input(f'Please enter number {num + 1}: '))
    numbers.append(ask_num)

#check each number if it duplicates
for counter in numbers:
    if numbers.count(counter) == 1:
        no_duplicates.append(counter)

#print results
print (no_duplicates)