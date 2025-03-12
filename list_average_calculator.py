#Prog05: Create a program that ask user to input a number, continue asking until 
# the user input is invalid. Display the average.

#create list
numbers = []

#ask user for numbers infinitely until invalid input
try:
    while True:
        ask_num = float(input("Please enter a number (non-numeric to finish): "))
        #add the asked number to list
        numbers.append(ask_num)
except ValueError:
    print('Invalid Input')
#calculate the average 
avg = sum(numbers)/len(numbers)

#print the result
print(f'The average of the numbers is {avg}')
