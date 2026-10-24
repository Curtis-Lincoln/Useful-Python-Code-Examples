#Basic Login System
username = "James"
password = "myPasswordIsDog!"
tries = 0

while tries < 3:
    user_in = input("Enter the username: ")
    pass_in = input("Enter the password: ")

    if user_in == username:
        if pass_in == password:
            print("Logged in")
            break
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")

    tries = tries + 1
