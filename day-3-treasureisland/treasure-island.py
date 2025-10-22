print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.")
road = input("You are at a cross road type 'left' to go left and 'right' to go right!\n").lower()
if road == 'left':
    pond = input("Now you arrived at a pond type 'swim' to swim across or 'wait' to wait for a boat\n").lower()
    if pond == 'wait':
        door = input("You arrived at a house, there is three door pick the one you want to cross by typing 'red', 'blue' or 'yellow'\n").lower()
        if door == 'yellow':
            print("Hurray you found the treasure, hope you will have a wonderful life! YOU WIN")
        elif door == 'red':
            print("You stepped into a fire pit! GAME OVER")
        elif door == 'blue':
            print("You stepped into a room full of beasts, and you become lunch! GAME OVER")
        else:
            print("There is no option like that!")
    elif pond == 'swim':
        print("A crocodile attacked you! GAME OVER")
    else:
        print("There is no option like that!")
elif road == 'right':
    print("You fall in a hole! GAME OVER")
