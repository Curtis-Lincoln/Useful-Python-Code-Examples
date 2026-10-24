#Lowest Number
#Example 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 <= num2:
    lowest = num1
else:
    lowest = num2

print("The lowest number is " + str(lowest))

#Example 2
def lower_num(num1,num2):
    if num1 <= num2:
        lowest = num1
    else:
        lowest = num2

    print("The lowest number is " + str(lowest))

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

lower_num(first_num,second_num)

#Example 3
def Lower_num(num1,num2):
    if num1 <= num2:
        return num1
    else:
        return num2

First_num = int(input("Enter the first number: "))
Second_num = int(input("Enter the secind number: "))

Lowest = Lower_num(First_num,Second_num)

print("The lowest number is " + str(Lowest))
