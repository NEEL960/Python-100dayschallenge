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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('you\'re at a crossroad, where do you want to go? type "left" or "right"').lower()



if choice1 == 'left':
        #continue the game
        choice2=input('you have came to a lake. There is an island in the middle of the lake. type "Wait" to wait for a boat type "swim" to swim across')
        if choice2=='wait':
                #continue
                choice3=input('you arrive at an island and hand there is a house with three door, one red one yellow and one blue which colour do you choose?').lower()
                if choice3 =='red':
                        print('Game over its room of fire')
                elif choice3=='yellow':
                        print('you found treasure, you win the game')
                elif choice3=='blue':
                        print('you are dying in a lack of water game over')
                else:
                        print("no door exist game over")
        else:
                print ('You have died in your attempt, game over')
else:
        print('game over, fell into the hole ')
