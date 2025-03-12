#Prog03: Create a program that ask user to input a number, continue asking until
#  the user input is invalid. Display the highest number

#create list
numbers = []

#ask for numbers infinitely until invalid
try:
    while True:
        ask_num = float(input('Please enter a number: '))
        numbers.append(ask_num)
except ValueError:
    print ("Invalid Input")
#sort list to reverse and print the first number
    numbers.sort(reverse=True)
    print (numbers)
    print (f'The highest number in the list is {numbers[0]}.')