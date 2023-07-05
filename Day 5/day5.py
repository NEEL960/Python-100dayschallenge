fruits =['apple','banana','lychee']
for i in fruits:
    print(i)
    print(i + 'pie')


#------------------------- write a program that calculates the average student height from a List of heights.
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# length=len(student_heights)
# total=sum(student_heights)
# Avg_height= total/length
# print(Avg_height)


# # with for loop method 
# total_height=0
# for h in student_heights:
#     total_height +=h
# print(total_height)

# no_students=0
# for i in student_heights:
#     no_students +=1
# print(no_students)

# avg_h= round(total_height/no_students)
# print(avg_h)


#------------------------------------------------------------------------------------
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_no=0
print(max_no)

for i in student_scores:
    if i > max_no:
        max_no=i
    
print(f'the highest score is {max_no}')



#---------------------------
total=0
for number in range(1,101):
    total +=number

print(total)



#----------------------------------You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#Write your code below this row 👇
total=0
for number in range(2,102,2):
    total +=number
    #print(number)

print(total)





#Write your code below this row 👇 ----You are going to write a program that automatically prints the solution to the FizzBuzz game

for i in range(1,101):
    if (i%3==0 and i%5==0):
        print('fizzbuzz')
    elif (i%5==0):
        print('buzz')
    elif (i%3==0):
        print('fizz')
    else:
        print(i)
