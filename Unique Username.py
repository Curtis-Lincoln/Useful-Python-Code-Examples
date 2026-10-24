#Unique Username
def generate_username(firstname, lastname):
    #create username based on the lastname and first intial
    username = lastname + firstname[0]

    #open the file in read mode and evaluate its contents
    users_file = open("users.txt","r")
    usernames = eval(users_file.read())
    users_file.close()

    #check the entire 2D array to see if the username exists
    for count in range(len(usernames)):
        #if the username exists, add a # symbol
        if usernames[count][0] == username:
            username = username + "#"

    #return the final username
    return username

forename = input("Enter your first name: ")
surname = input("Enter your surname: ")

username_out = generate_username(forename, surname)
print("Your username is " +str(username_out))
