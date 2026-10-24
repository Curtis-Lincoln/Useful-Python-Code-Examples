#Weak Password?
obvious = ["password", "qwerty", "hello123", "letmein", "123456"]

password = input("Please enter a password: ")

#A basic linear search which iterates through the obvious
#list to check for matches against the password

for count in range(len(obvious)):
    if password == obvious[count]:
        print("""This password is weak. It uses a common word or phrase making
                 it susceptible to a brute force attack""")

    #Length check
    if len(password) < 8:
        print("Your password is too short. Please use at least 8 characters")

    #initialise some counter variables for different types of characters

    char = 0
    num = 0
    upper = 0
    lower = 0

    for count in range(len(password)):
        #A linear search to check if the character is a digit
        if password[count].isdigit():
            num = num + 1
        #A check to see if the character is an upper or lower char
        elif password[count].isalpha():
            char = char + 1
            if password[count].isupper():
                upper = upper + 1
            elif password[count].islower():
                lower = lower + 1

if num == 0:
    print("To make your password more secure, you could include numbers")
if upper == 0 or lower == 0:
    print("To make your password more secure, you could include upper and lower case letters")
if char == 0:
    print("To make your password more secure, you could include letters")
if num > 0 and char > 0 and upper > 0 and lower > 0:
    print("""Your password meets the minimum length requirements and contains
                 a mixture of numbers, characters, upper and lower case letters.""")
        



  
