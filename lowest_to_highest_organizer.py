#Prog05: Create a program that ask user to input a number, continue asking until the user
#  input is invalid. Display the number from lowest to highest. Clue: sort() function

#create list
numbers = []

#ask for numbers infinitely until invalid
try:
    while True:
        ask_num = float(input('Please enter a number: '))
        numbers.append(ask_num)
except ValueError:
    print ("Invalid Input")
#sort list and print
    numbers.sort()
    print (numbers)