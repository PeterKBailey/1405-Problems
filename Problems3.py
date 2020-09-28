#Question 1
check = True
while check == True:
        print("(A)ddition \n(S)ubtraction \n(M)ultiplication \n(D)ivision (Long)")
        choice = input("Please select an operation from the list above: ")
        a = int(input("Please provide the 1st integer: "))
        b = int(input("Please provide the 2nd integer: "))
    
        if choice == "A" or choice == "a":
            print(a, "+", b, "=",a+b)
        elif choice == "S" or choice == "s":
            print(a,"-",b,"=",a-b)
        elif choice == "M" or choice == "m":
            print(a,"*",b,"=",a*b)
        elif choice == "D" or choice == "d":
            print(a,"/",b,"=",a//b," remainder ",a%b)
        else:
            print("We're done here.")
            check = False
#Question 2
year = int(input("What year would you like to check?, q to quit"))
while(True):
    try:
        if year%4 == 0 and year%400 != 0 and year%100 !=0:
            print(year, " is a leap year")
        else:
            print(year, "is not a leap year")
        year = int(input("What year would you like to check?, q to quit"))
    except:
        break

    

    