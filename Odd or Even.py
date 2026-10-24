#Odd or Even?
def is_odd(number_in):
    if int(number_in) %2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

again = True
while again:
    number = input("Enter a number: ")

    if number != "STOP" :
        odd = is_odd(number)
    else:
        again = False
