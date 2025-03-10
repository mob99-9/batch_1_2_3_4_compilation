#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
number = 0
while number < 101:
    if number % 2 == 0:
        number += 1
    else:
        print(number)
        number += 1