#question 1:
def lettercount(str):
    dict = {}
    for x in str:
        if x in dict:
            dict[x]=dict[x]+1
        else:
            dict[x]=1
    return dict
    
print(lettercount("ababsssbbt"))

#question 2:
def factorial(flint):
    fact = 1
    for x in range(1,flint+1):
        fact *= x
    return fact
print(factorial(7))

def cachedFactorial(flint,dict):
    highestFact = 1
    highestVal = 0
    fact = 1
    #all values up until flint
    for x in range(1,flint+1):
        #if we know the factorial of a value before flint
        if x in dict:
            #then that value replaces the highest facotial known   
            highestFact = dict[x]
            highestVal = x
    print('the highest: ', highestFact)
    for x in range(flint,highestVal,-1):
        fact *= x
    fact*=highestFact
    dict[flint] = fact
    return fact

dictFact = {}
print(cachedFactorial(5,dictFact))
print(cachedFactorial(7,dictFact))

#question 3:
morse_code = {
  'A': '.-',
  'B': '-...',
  'C': '-.-.',
  'D': '-..',
  'E': '.',
  'F': '..-.',
  'G': '--.',
  'H': '....',
  'I': '..',
  'J': '.---',
  'K': '-.-',
  'L': '.-..',
  'M': '--',
  'N': '-.',
  'O': '---',
  'P': '.--.',
  'Q': '--.-',
  'R': '.-.',
  'S': '...',
  'T': '-',
  'U': '..-',
  'V': '...-',
  'W': '.--',
  'X': '-..-',
  'Y': '-.--',
  'Z': '--..',

  '0': '-----',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.',

  ' ': '     '
}



def stringtomorse(str):
    str2 = ""
    for x in str:
        if x in morse_code:
            str2 += morse_code[x]
            str2 += " "
    return str2

    
    
str = input("What to convert?").upper()    
print(stringtomorse(str))

#question 4 i think
def jsontoDict(str):
    x = str.strip("{").strip("{").strip('"')
    dict = {}
    while x.find('"')!=-1:
        key = x[:x.find('"')]
        
        x = x[x.find('"')+1:]
        x = x[x.find('"')+1:]

        val = x[:x.find('"')]
        dict[key] = val
        
        x = x[x.find('"')+1:]
        x = x[x.find('"')+1:]
    return dict
print(jsontoDict('{"key1":"value1","key2":"value2","keyn":"valuen"}'))

#problem 5 or so
def load(name):
    f = open(name,"r")
    dict = {}
    x = []
    line = f.readline()
    contents = ""
    
    while line!="":
        contents+=line
        line = f.readline()
    x = contents.split(" ")
    f.close()
    return x,dict
    
    
def commonword(a):
    x,dict = load("testfile1.txt")
    for word in x:
        for search in a:
            if search == word:
                if search in dict:
                    dict[search]+=1
                else:
                    dict[search]=1
    if len(a)==0 or len(dict)==0:
        return None
    return dict

def commonpair(str):
    x,dict = load("testfile1.txt")
    #every index in the list of words
    for i in range(len(x)):
        #if we're not at the last word
        if i != len(x)-1:
            #if the current word is the word given
            if x[i] == str:
                #add the following word to dictionary and add 1 to its element
                if x[i+1] in dict:
                    dict[x[i+1]]+=1
                else:
                    dict[x[i+1]]=1
                print(dict)
    #if there are no words following
    if len(dict) == 0:
        return None
    return dict
                
def countall():
    x,dict = load("testfile1.txt")
    return len(x)

def countunique():
    x,dict = load("testfile1.txt")
    for word in x:
        if word not in dict:
            dict[word] = 1
    return len(dict)

list = ["peach","banana"]
#print(commonword(list))
#print(commonpair("peach"))
#print(countall())
print(countunique())
