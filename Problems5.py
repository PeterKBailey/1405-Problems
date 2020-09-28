#Problem 1
def isMultiple(a,b):
    if b%a==0:
        return True
    else:
        return False
        
def commonMultiple(a,b,c):
    one = isMultiple(a,c)
    two = isMultiple(b,c)
    if one and two:
        return True
    else:
        return False

a = int(input("first number"))
b = int(input("second number"))

for x in range(1,101):
    if commonMultiple(a,b,x):
        print(x, " is a common multiple")
        
#problem 4
def pow2(a):
    ans = 0
    while 2**ans<a:
        ans+=1
    if 2**ans>a:
        ans-=1
    return 2**ans
    
def decToBin(x):
    p = pow2(x)
    outPut = "0b"
    while p!=0:
        if p<=x:
            x=x-p
            outPut+="1"
        else:
            outPut+="0"
        p=p//2
        
    return outPut
    
print(decToBin(200))
print(bin(200))