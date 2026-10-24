#Unlimited Pin Attempts
pin = ""
while pin != "1984":
    pin = input("Please enter the pin: ")

    if pin == "1984":
        print("Logged in ")
    else:
        print("Incorrect pin")
