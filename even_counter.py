#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
for number in range(0,101):
    if number % 2 == 0:
        print(number)
    else:
        continue