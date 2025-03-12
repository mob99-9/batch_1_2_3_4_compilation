#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#create lists
numbers = []
duplicates = []

#ask user for 10 numbers and add to list
for number in range(0,10):
    ask_num = float(input(f'Please enter number {number + 1}: '))
    numbers.append(ask_num)

#check for duplicates 
for num in numbers:
    if numbers.count(num) != 1:
        duplicates.append(num)
    else:
        None

#print the numbers with duplicates
print (f'The duplicated numbers are {duplicates}')
print (f'\nThe duplicated numbers are {set(duplicates)}')