#Roll a double to start
import random

#initialise the dice with two different value so the program runs at least once

dice1 = 1
dice2 = 2

while dice1 != dice2:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("Dice 1 rolled :" + str(dice1))
    print("Dice 2 rolled :" + str(dice2))

    if dice1 == dice2:
        print("Game loading")
    else:
        #Use input to enable the user to press enetr to continue looping

        again = input("Press enetr to roll again ")
