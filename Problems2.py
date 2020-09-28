#from SimpleGraphics import *
#question 1,2, and 3
age = input("Whats ur age?")
age = int(age)
print(age+5)

#question 4
USD = float(input("How many us dollas u got?"))
CAD = 0.76*USD
print(USD, "$ USD = $",CAD," CAD")

#Question 5
dimensions = [0,0,0]
for x in range(0,3):
    dimensions[x] = input("gimme the next dimension")
    dimensions[x] = int(dimensions[x])

print("The volume of rectangular prism ", dimensions[0],"x",dimensions[1],"x",dimensions[2], "= ", dimensions[0]*dimensions[1]*dimensions[2])

#Question 6
grades = [0,0,0,0]

for count in range(0,3):
   grades[count] = input("Enter midterm grade")
   grades[count] = int(grades[count])*0.2
   
grades[3] = input("Enter Exam grade")
grades[3] = int(grades[3])*0.4

finalGrade = 0;
for count in range(0,4):
    finalGrade = finalGrade + grades[count]
    
print("Your final grade is ", finalGrade)


#Question 7
import random

guessNum = random.randint(1,100)
guess = int(input("guess the number!"))

if guess == guessNum:
    print("You got it!")
else:
    print("Wrong!!")
    diff = abs(guess-guessNum)
    print("You were ", diff, " away")

#Question 8
