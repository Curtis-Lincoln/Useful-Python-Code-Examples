#Highest Number
#define a function called highest_num with three parameters
def highest_number(num1, num2, num3):
    #return the highest number
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

#call the highest_number function and pass the contents of
#first, second and third variables as arguments into the
#parameters num1, num2, num3
highest = highest_number(first, second, third)

#output the highest number with a meaningful message
print("The highest number is " + str(highest))
