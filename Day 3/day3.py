# if else 

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight1= float(weight)
height1= float(height)*float(height)
BMI= weight/height*height
#BMI= (weight1/height1)
print(int(BMI))

if BMI > 35:
    print("they are clinically obese")
elif 35 > BMI > 30:
    print("they are obese")
elif 30 > BMI > 25:
    print("they are slightly overweight")
elif 25 > BMI > 18.5:
    print("they have a normal weight")
else:
    print(" they are underweight")



#>= greater than equal to
#> greater than
#< lesser than 
#<= lesser than equal to


## -------Leap year ------------------
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")


##-----------------Mutliple if else----------------------
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# final_bill=0

# if extra_cheese=='Y':
#     final_bill +=1
# else:
#     final_bill =0

# if size=='S':
#     final_bill += 15
#     if add_pepperoni == 'Y':
#         final_bill +=2
#     else:
#         final_bill ==15
# elif size=='M':
#     final_bill +=20
#     if add_pepperoni == 'Y':
#         final_bill +=3
#     else:
#         final_bill ==20
# else:
#     final_bill +=25
#     if add_pepperoni == 'Y':
#         final_bill +=3
#     else:
#         final_bill==25

# print(f"Your final bill is: ${final_bill}")


##--------------love  calculator--------------------
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# name1.lower()
# name2.lower()
# name1.count('t','r','u','e','l','o','v','e')
# name2.count('t','r','u','e','l','o','v','e')

# combined_string= name1+name2
# lower_case= combined_string.lower()

# t=lower_case.count('t')
# r=lower_case.count('r')
# u=lower_case.count('u')
# e=lower_case.count('e')

# true =t+r+u+e

# l=lower_case.count('l')
# o=lower_case.count('o')
# v=lower_case.count('v')
# e=lower_case.count('e')

# love= l+o+v+e

# love_score = int(str(true)+ str(love))

# print(love_score)

# if love_score < 10 or love_score > 90:
#     print(f"your love score is {love_score}, you go together like coke and mentos")
# elif love_score >=40 and love_score <=50:
#     print(f"your love score is {love_score}, you are alright together")
# else:
#     print(f'your score is {love_score}')