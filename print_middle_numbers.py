#Prog10: Create a program that ask user to input 2 numbers. 
# Print all the numbers between the two numbers.
num_1 = int(float(input('Enter the first number: ')))
num_2 = int(float(input('Enter the second number: ')))
for num in range (num_1 + 1, num_2):
    print(num)