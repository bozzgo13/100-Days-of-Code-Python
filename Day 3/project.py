# link to the chart https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D


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

choice1 = input("Where do you want to go? Left or Right: ").upper()

if choice1 == "LEFT":
    print("Good choice.")
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across the lake: ").upper()

    if choice2 == "WAIT":
        print("You chose well.")
        print("Ten minutes later, a small wooden boat appears and picks you up.")
        print("The fisherman drops you off at the island's shore.")

        print("In the center of the island, you find a mysterious stone house.")
        print("There are three doors in front of you: RED, YELLOW, and BLUE.")
        choice3 = input("\nWhich door will you open? (RED / YELLOW / BLUE): ").upper()

        if choice3 == "RED":
            print("\nYou open the red door and step inside...")
            print("The room is filled with magical flames! You burn to ashes instantly.")
            print(" GAME OVER ".center(30, "-"))
            print("Your journey ends here.")
        elif choice3 == "BLUE":
            print("\nYou open the blue door and enter a dark room...")
            print("A hungry lion leaps from the shadows and attacks you!")
            print(" GAME OVER ".center(30, "-"))
            print("Your journey ends here.")
        elif choice3 == "YELLOW":
            print("\nYou slowly push open the yellow door...")
            print("\nCONGRATULATIONS!")
            print("The room is filled with gold coins and sparkling gems.")
            print("You have found the legendary treasure!")
            print("You will live in wealth for the rest of your life.")
            print(" YOU WIN! ".center(30, "-"))

    else:
        print("You dive into the cool water. At first, it feels refreshing. You stroke powerfully.")
        print("But halfway there, the current changes. The peaceful waves turn into heavy walls of water.")
        print("Your muscles begin to burn. Your lungs scream for air.")
        print("You made a bad decision. After all, you know you're not that good of a swimmer.")
        print(" GAME OVER ".center(30, "-"))
        print("Your journey ends here.")
else:

    print("You have been wandering the desert for three days.")
    print("There is not a soul in sight.")
    print("You have run out of food and water.")
    print(" GAME OVER ".center(30, "-"))
    print("Your journey ends here.")
