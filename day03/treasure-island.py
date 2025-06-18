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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

where_to_go = input("You are at a cross road. Where do you want to go? \n    Type 'left' or 'right' \n").capitalize()



if where_to_go == "Left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. \n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").capitalize()
    if swim_or_wait == "Wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. \n   One red, one yellow and one blue. Which color do you choose?\n").capitalize()
        if door == "Yellow":
            print("You win!")
        elif door == "Red":
            print("Burned by fire. Game Over.")
        elif door == "Blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")