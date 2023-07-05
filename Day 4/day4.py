##--------------heads tails --------------------
# import random

# random_integer= random.randint(0,1)
# print(random_integer)

# if random_integer==0:
#     print('tails')
# else:
#     print("heads")


# ###--------------Random decimal number between 0 to 5--------------------
# random_float= random.random()*5 
# print(random_float)

##--------------lists --------------------

# fruits=["item1","item2"] #----> example

# states_of_america=['delaware','pennsylvania','texas']
# print(states_of_america[0])


#   data structure --> .append


#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# import random
# people =['angela','ben','jenny','chloe','michael']
# index=random.randrange(len(people))
# bill= people[index]
# print(f'{bill} is going to buy the meal today')


# # Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# import random
# num_items=len(names)

# random_choice=random.randint(0,num_items-1)
# person_who_will_pay=names[random_choice]
# print(person_who_will_pay+' is going to buy meal today')


###-----------------------------------------treasure game putting x in position (bit confused )
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#23--> first column and then row 
#Write your code below this row 👇
horizontal = int(position[0]) #2
vertical = int(position[1])  #3

selected_row= map[vertical-1]
selected_row[horizontal-1] ='x'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

