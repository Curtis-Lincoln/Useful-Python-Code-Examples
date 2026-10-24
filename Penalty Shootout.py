#Penalty Shootout
import random

keeper = ["left", "centre", "right"]

keeper_score = 0
player_score = 0

for count in range(5):
    dive = random.choice(keeper)

    player = input("Do you wish to shoot to the left, centre or right: ")

    print("Keeper went to the", dive)

    if keeper == player:
        print("Penalty saved")
        keeper_score = keeper_score + 1
    else:
        print("GOAAAAAAL!")
        player_score = player_score + 1

if keeper_score > player_score:
    print("Keeper wins", keeper_score, "-", player_score)
else:
    print("You win!", player_score, "-", keeper_score)
