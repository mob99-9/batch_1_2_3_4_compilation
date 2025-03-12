#Prog02: Create a program that ask user to input 10 numbers.
#Display all numbers. For numbers with duplicate, display only the first entry.

#create list
numbers = []

#ask for 10 numbers
for num in range(0,10):
    ask_num = float(input(f'Please enter number {num + 1}: '))
    numbers.append(ask_num)

#print the modified list that makes duplicates uncountted
print (set(numbers))