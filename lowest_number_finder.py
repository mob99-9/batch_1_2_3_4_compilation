#Prog04: Create a program that ask user to input a number, continue asking until 
# the user input is invalid. Display the lowest number

#create list
numbers = []

#ask for numbers infinitely until invalid
try:
    while True:
        ask_num = float(input('Please enter a number: '))
        numbers.append(ask_num)
except ValueError:
    print ("Invalid Input")
#sort list and print the first number
    numbers.sort()
    print (numbers)
    print (f'The smallest number in the list is {numbers[0]}.')