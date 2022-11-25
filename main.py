from time import sleep
import pygame

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
sleep(1)
print("Your mission is to find the treasure!")
sleep(1)
choice1 = input("You're at a crossroad, where you want to go? Type 'left' or 'right'?\n").lower()
sleep(1)
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    sleep(1)
    if choice2 == "wait":
        choice3 = input("You arrive at the island unarmed. There is a house with 3 doors.\n"
                        "One red, one yellow and one blue. Witch door do you chose?\n").lower()
        sleep(1)
        if choice3 == "Red":
            print("Its a room full of fire. Game Over.")
            sleep(1)
        elif choice3 == "Yellow":
            print("You find the treasure! You Win!")
            sleep(1)
        elif choice3 == "Blue":
            print("You enter in room full of beasts. Game Over.")
            sleep(1)
        else:
            print("You chose a door that doesn't exist. Game Over.")
            sleep(1)
    else:
        print("You were attacked by angry trout. Game Over.")
        sleep(1)
else:
    print("You fall into a hole. Game Over.")
    sleep(1)
