#Login System By Reading a 2D List in a File
def login():
    username = input("What is your username: ")
    password = input("What is your password: ")

    newfile = open("users.txt","r")
    users_2D = eval(newfile.read())
    newfile.close()

    found = False
    for count in range(len(users_2D)):
        if username == users_2D[count][0]:
            found = True
            if password == users_2D[count][1]:
                print("logged in")
            else:
                print("incorrect password")
                login()

    if found == False:
        print("Invalid username")
        login()

login()
