#String Concatenation: Making a Username
#Example 1
def user_name(forename, last_name, year):
    username_out = year[2:4] + forename[0] + last_name

    print("Your username is " + username_out)

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
joined = input("Enter the year you joined the school: ")

user_name(first_name,surname,joined)

#Example 2
def User_name(forename, last_name, year):
    username_out = year[2:4] + forename[0] + last_name

    return username_out

def main():
    first_name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    year = input("Enter the year you joined the school: ")

    gen_user_name = User_name(first_name , surname, year)
    print("Your username is " + gen_user_name)

if __name__ == '__main__':
    main()
