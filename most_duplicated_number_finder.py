#Prog02: Create a program that ask user to input a number, continue asking 
# until the user input is invalid. Display the number with the most number of duplicate.

#create list
numbers = []

#ask for numbers infinitely until invalid
try:
    while True:
        ask_num = float(input('Please enter a number: '))
        numbers.append(ask_num)
except ValueError:
    print ("Invalid Input")
#assign for the variable of the most duplicate 
most_duplicate = 0
most_number = 0

#count the duplicate
for number in numbers:
    dupli = numbers.count(number)
    if dupli > most_duplicate:
        most_duplicate = dupli
        most_number = number
    else:
        None
#print the results
print (f'The most duplicated number is {most_number} with {most_duplicate} duplicates')