rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("ROCK PAPER SCISSORS")

play= int(input('What do you choose? Type 0 for rock type 1 for paper or two for scissor?\n'))
# play_1=[0,1,2]
# rock =0
# paper =1
# scissors=2

# if rock==play_1[0]:
#     print(rock)
# else:
#     print(paper)
# else:
#     print(scissors)
# else scissors==2:
#     print(scissors)

if play==0:
    print(rock);
elif play==1:
    print(paper)
elif play==2:
    print(scissors)

import random

print("Computer chose: ")

computer=[0,1,2]
computers=(random.randint(0,len(computer)-1))

if computers==0:
    print(rock)
elif computers==1:
    print(paper)
elif computers==2:
    print(scissors)

##---> logic of the game

if play==computers:
    print('match draw')
elif play==0 and computers==2 or play>computers:
    print('You win')
elif play==2 and computers==0 or computers>play:
    print('You lose')










# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# else:
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end