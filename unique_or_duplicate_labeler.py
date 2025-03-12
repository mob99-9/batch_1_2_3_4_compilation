#Prog03: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. Display "Unique" 
# after input when the inputted number don't have duplicate. Display "Duplicate" 
# after input when the inputted number have duplicate.

#create list 
numbers = []

#ask for numbers infinitely until invalid 
try:
    while True:
        ask_num = float(input('Please enter a number: '))
        numbers.append(ask_num)
        
#assign each number
except ValueError:
    for number in numbers:
        if numbers.count(number) == 1:
            print (f'{number}: Unique')
        else:
            print (f'{number}: Duplicate')