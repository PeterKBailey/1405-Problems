#Question one!
x = int(input("Gimme a number"))
y=1
sum = 0
while y!=x+1:
    if x%y==0:
        print(y," is a divisor")
        sum += y
    y+=1
print(sum, " is the sum of all divisors")
if sum == (x+1):
    print("the number is prime")
else:
    print("Not prime")
#part b
x = int(input("gimme the number"))
sum = 0
for i in range(1,x+1):
    if x%i==0:
        print(i, " is a divisor of ", x)
        sum +=i
print("The sum is ", sum)
if sum == (x+1):
    print("the number is prime")
else:
    print("Not prime")
    
#Question two
dryDays=0
while dryDays<3:
    didRain = input("It rained today?")
    if didRain == "True":
        dryDays = 0
    else:
        dryDays += 1
print("Quick! water the garden!")

#Question three
x = int(input("Give me the number"))
count = 0
while x!=0:
    x = x//10
    count += 1
print("There are ", count, " digits")

#Question four
fileName = input("Which file? studentinfoX.txt")
f = open("studentinfo0.txt","r") #this can be interpreted as an array

firstname = f.readline().strip()

numPass = 0
numFail = 0
bestGrade = 0
bestName = ""
worstGrade = 100
worstName = ""
sum = 0
count = 0
while firstname!="":
    lastname = f.readline().strip()
    id = int(f.readline().strip())
    assignment = int(f.readline().strip())
    midterm = int(f.readline().strip())
    exam = int(f.readline().strip())
    
    final = 0.25*assignment+0.25*midterm+0.5*exam
    
    if final >= 50 and exam >= 50:
        numPass += 1
    else:
        numFail +=1
    
    if final>bestGrade:
        bestGrade = final
        bestName = firstname + lastname
        
    if final<worstGrade:
        worstGrade = final
        worstName = firstname + lastname
        
    sum+=final
    firstname = f.readline().strip()
    
print("the average is ", sum/(numPass+numFail))
print(numPass, ' passed ', numFail, " Failed")
print(bestName, " was best with ",bestGrade,"%")
print(worstName, " was worst with ", worstGrade,"%")
f.close()

#Question 5
f = open("numbertest0.txt","r")

sum = 0
bif = 0
small = 0
pos = 0
neg = 0
count = 0

line = f.readline().strip()

while line!="":
    if int(line)>0:
        pos+=1
    elif int(line)<0:
        neg+=1
    if int(line)>bif:
        bif = int(line)
    if int(line)<small:
        small = int(line)
    sum+=int(line)
    count+=1
    line = f.readline().strip()
    
print("Average: ", sum/count)
print("Positive: ", pos)
print("Negative: ", neg)
print("Biggest: ", bif)
print("Smallest: ", small)
f.close()

#Question 6
name = input("What's ur name?")

choice = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
sum = 0

while True:
    print("1. Desktop Computer ($850 each)")
    print("2. Laptop ($1225 each)")
    print("3. Tablet ($600 each)")
    print("4. Toaster Oven ($85 each)")
    print("Anything else to exit")
    
    choice = input("which one?")    
    if int(choice) == 1:
        howMany = int(input("How many u want broseph"))
        num1+=howMany
        sum+=(850*howMany)
    elif int(choice) == 2:
        howMany = int(input("How many u want broseph"))
        num2+=howMany
        sum+=(1225*howMany)
    elif int(choice) == 3:
        howMany = int(input("How many u want broseph"))
        num3+=howMany
        sum+=(600*howMany)
    elif int(choice) == 4:
        howMany = int(input("How many u want broseph"))
        num4+=howMany
        sum+=(85*howMany)
    else:
        break

        
        
print(name, " here is your receipt")
print("---------------------------")
print(num1, " Desktop Computer")
print(num2, " Laptops")
print(num3, " Tablets")
print(num4, " Toaster Oven")
print("---------------------------")
print("Total cost: $", sum,"\nGet out of here you shit")

#Question 7
#a)
current = input("positive integer, q to quit")
count = 1
max = 0
while current!="q":
    prev = current
    current = input("positive integer, q to quit")
    if current=="q":
        if count>max:
            max = count
        break
    if int(current)>int(prev):
        count+=1
    elif int(current)<int(prev):
        if count>max:
            max = count
        count = 1
    
print(max)

#b)
f = open("numbertest0.txt","r")
og = 0
count = 1
max = 0
for line in f:
    if int(line)>og:
        count+=1
    elif int(line)<og:
        count=1
    if count>max:
        max = count
    og = int(line)
    
print(max)
