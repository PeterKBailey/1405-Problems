#Question 1
def multiply(a,b):
    if b == 1:
        return a
    return a+multiply(a,b-1)

print(multiply(3,4))

#Question 2
def reverse(str):
    if len(str) == 1:
        return str
    return reverse(str[1:])+str[0]
print(reverse("hi there"))

#Question 3
def mergelists(a,b):
    c = []
    helper(a,b,c)
    return c

def helper(a,b,c):
    #print(c)
    if len(b)==0:
        return c.extend(a)
    if len(a)==0:
        return c.extend(b)
    else:
        if a[0]>=b[0]:
            c.append(b.pop(0))
        elif b[0]>a[0]:
            c.append(a.pop(0))
        return helper(a,b,c)
            
print(mergelists([0, 2, 4, 6, 6, 8, 9, 9], [0, 1, 3, 5, 6, 7, 9]))

#Question 5
def cachedfactorial(x,dict):
    print(x)
    if x in dict:
        return dict[x]
    if x == 1:
        return x
    else:
        b = x*cachedfactorial(x-1,dict)
        if x not in dict:
            dict[x] = b
        return b

dict = {}
print(cachedfactorial(8,dict))
print(dict)
print(cachedfactorial(5,dict))
print(cachedfactorial(10,dict))