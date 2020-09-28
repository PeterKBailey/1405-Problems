#question 1
b = [1,3,4,6,7,7]

def mergeAndSort(a,b):
    indexA = 0
    indexB = 0
    newList = []
    for x in range(len(a)+len(b)):
        if a[indexA]<b[indexB]:
            newList.append(a[indexA])
            indexA+=1
        elif a[indexA]>b[indexB]:
            newList.append(b[indexB])
            indexB+=1
        else:
            newList.append(a[indexA])
            indexA+=1
        if indexA == len(a):
            newList += b[indexB:]
            break
        elif indexB == len(b):
            newList += a[indexA:]
            break
    return newList

#question 3
def maxvalue(a):
    max = 0
    for x in a:
        if x>max:
            max = x
    return max
    
#question 4
def maxvolume(a):
    max = 0
    for x in a:
        volume = 1
        for y in x:
            volume = volume*y
        if volume>max:
            max = volume
    return max
    
#question 5
def topx(a,x):
    b = [0]*x
    for j in range(x):
        max = 0
        for i in range(len(a)):
            if a[i] > a[max]:
                max = i
        b[j] = a.pop(max)
    return b
    
#question 7
def masterMind():
    import random
    code = []
    for x in range(5):
        code.append(random.randint(0,10))
    print(code)
    for x in range(10):
        numRight = 0
        guess = input(str(10-x)+" guesses remaining! > ")
        guessN = []
        for y in guess:
            guessN.append(int(y))
        for i in range(len(guessN)):
            if guessN[i]==code[i]:
                numRight+=1
        print(numRight," out of 5 correct!")
        if numRight==5:
            print("you got it!")
            break
    print("The code was: ", code)
    
#question 8
global maxSize
maxSize = 10
def enqueue(a,n):
    if len(a)<maxSize:
        a.append(n)
        return True    
    return False
        
def dequeue(a):
    if isEmpty(a)==False:
        return a.pop(0)
    return None
    
def peek(a):
    if isEmpty==False:
        return a[0]
    return None

def isEmpty(a):
    if len(a)==0:
        return True
    return False

def multiEnqueue(a,b):
    indexB = 0
    
    for i in range(len(a),maxSize):
        try:
            a.append(b[indexB])
            indexB+=1
        except:
            break
    return indexB

def multiDequeue(a,n):
    b = []
    for i in range(n):
        if len(a)!=0:
            b.append(a.pop(0))
    return b
         
a = [1,4,2,5,7,4,2,6,3]
b = [5,3,6]
c = []
d = [1,4,2,5,7,4,2,6,3]
e = [5,3,6]
print(enqueue(a,4))#True
print(enqueue(a,5))#False
print(dequeue(a)," ",a)#1, a without 1
print(dequeue(c)," ",c)#None, []
print(peek(d)," ",d)#1, d with 1
print(peek(c)," ",c)#None, []
print(isEmpty(a))#False
print(isEmpty(c))#True
print(multiEnqueue(d,b),d)#1
print(multiEnqueue(b,d),b)#7
print(multiDequeue(d,4))#[1,4,2,5]
print(multiDequeue(e,4))#[5,3,6]

#Questions 9 and 10
def push(stack,n):
    stack.append(n)

def pop(stack):
    if len(stack)>0:
        return stack.pop()
    return None
 
def peak(stack):
    if len(stack)>0:
        return stack[len(stack)-1]
    return None
    
def isValid(str):
    stack = []
    for s in str:
        if s == "{" or s == "(" or s == "[":
            push(stack,s)
        elif s == "}" and peak(stack) == "{":
            pop(stack)
        elif s == ")" and peak(stack) == "(":
            pop(stack)
        elif s == "]" and peak(stack) == "[":
            pop(stack) 
        else:
            return False
    return True
   
print(isValid("{{}}"))#True
print(isValid("{[][]}"))#True
print(isValid("([)"))#False
print(isValid("([)]"))#False

#question 11
def startwords(str):
    a = str.split(". ")
    b = []
    c = []
    for x in a:
        b = x.split(" ")
        c.append(b[0])
    return c

def endwords(str):
    a = str.split(" ")
    b = []
    for x in a:
        if x.find(".")>0:
            b.append(x.strip("."))
    return b
print(startwords("This is a sentence. The previous sentence had four words."))
print(endwords("This is a sentence. The previous sentence had four words."))

#question 12
def jsontolist(str):
    strN = ""
    for x in str:
        if x!='"':
            strN+=x
    a = strN.strip("{").strip("}").split(",")
    b = []
    for x in a:
        b.append(x.split(":"))
    return b
    
list = jsontolist('{"firstname":"dave","lastname":"mckenney","position":"instructor"}')
print(list)
def getvalue(list,key):
    for x in list:
        if x[0] == key:
            return x[1]
print(getvalue(list,"lastname"))

#Question 15
def isgameover(board):
    count = 0
    boardDim = len(board)

    #row
    for row in board:        
        first = row[0]
        if first == "":
            continue
        count = 0
        for square in row:
            if square == first:
                count+=1
            else:
                break
        if count == boardDim:
            return True
    
    #col
    for i in range(boardDim):
        first = board[0][i]
        if first == "":
            continue
        count = 0
        for j in range(boardDim):
            if board[j][i] == first:
                count +=1
        if count == boardDim:
            return True
    
    #diagonal
    first = board[0][0]
    count = 0
    for i in range(boardDim):
        if first == "":
            break
        if board[i][i]==first:
            count+=1
    if count == boardDim:
        return True
    
    #diagonal
    first = board[0][boardDim-1]
    count = 0
    for i in range(boardDim):
        if first == "":
            break
        if board[i][boardDim-1-i] == first:
            count+=1
    if count == boardDim:
        return True
    return False
    
def printBoard(board):
    for x in board:
        print(x)

def resetBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = ""
            
def emptySpot(board,row,col):
    if row>=len(board) or col>=len(board) or board[row][col] != "":
        return False
    return True

def full(board):
    for i in board:
        for j in i:
            if j == "":
                return False
    return True

def play(board):
    playAgain = True
    
    while playAgain:
        round = 1
        resetBoard(board)
        while True:
            printBoard(board)

            if isgameover(board):
                if round%2!=0:
                    print("player 2 win")
                else:
                    print("player 1 win")
                break
            if full(board):
                print("tie")
                break
            row = int(input("gimme the row"))-1
            col = int(input("gimme the col"))-1
            if emptySpot(board,row,col):
                if round%2!=0:
                    board[row][col] = "x"
                else:
                    board[row][col] = "o"
                round+=1

            else:
                print("spot unavailable")                         
                
        again = input("again? y or n")
        playAgain = again=="y"
        
            
        
testB = [["","",""],["","",""],["","",""],]
play(testB)

