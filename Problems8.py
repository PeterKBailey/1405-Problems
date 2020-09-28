#problem 1
def GallopingSearch(list,search):
    start = 0
    end = 1
    while end < len(list) and list[end]<search:
        start = end
        end *= 2
    if end>len(list)-1:
        end = len(list)-1
    return binarySearch(list,search,start,end)
    
def binarySearch(list,search,start,end):
    while start<=end:
        mid = (start+end)//2
        if list[mid] == search:
            return True
        elif list[mid]> search:
            end = mid-1
        elif list[mid] < search:
            start = mid+1
    return False

#The complexity is O(log(n))
print(GallopingSearch([1,4,6,7,8,9,33],3))



#Question 2
#idk if this works
   # for i in range(len(uniqueL)):
     #   maxAt = 0
     #   for j in range(end):
      #      if uniqueL[j]>uniqueL[maxAt]:
      #          maxAt = j
       # temp = uniqueL[end]
       # uniqueL[end] = uniqueL[maxAt]
       # uniqueL[maxAt] = temp
        #end-=1
        
def CountingSort(list):
    dict = {}
    uniqueL = []
    for elem in list:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1
            uniqueL.append(elem)
    
    uniqueL.sort()
    sorted = []
    for elem in uniqueL:
        for y in range(dict[elem]):
            sorted.append(elem)
    return sorted
    

print(CountingSort([1,3,5,2,3,4,2,2,2,4,5,2,2]))


#Question 3
def quicksort(list):
    quicksorthelper(list, 0, len(list)-1)

     
def distance(point):
    return (point[0]**2+point[1]**2)**(1/2)
    
    	
def quicksorthelper(mylist, low, high):
	if low < high:
		p = partition(mylist, low, high)
		quicksorthelper(mylist, low, p)
		quicksorthelper(mylist, p+1, high)
	
def partition(mylist, low, high):
	pivot = distance(mylist[low])
	i = low - 1
	j = high + 1
	
	while True:
		i += 1
		j -= 1
		
		while distance(mylist[i]) < pivot:
			i += 1
		while distance(mylist[j]) > pivot:
			j -= 1
			
		if i >= j:
			return j
		
		mylist[i], mylist[j] = mylist[j], mylist[i]	
        
a =  [[2, 1], [2, 2], [3, 3], [3, 1], [1, 1], [1, 2]]        
quicksort(a)
print(a)

#Question 4
def count(list,value):
    start = findstart(list,value)
    end = findend(list,value)
    return(end-start+1)
    
def findstart(list,value):
    start = 0
    end = len(list)-1
    while start<=end:
        mid = (start+end)//2
        if (list[mid] == value and mid == 0) or (list[mid] == value and list[mid-1]!=value):
            return mid
        elif list[mid] < value:
            start = mid+1
        elif list[mid]>value or list[mid-1] == value:
            end = mid-1
    return -1
 
def findend(list,value):
    start = 0
    end = len(list)-1
    while start<=end:
        mid = (start+end)//2
        if (list[mid] == value and mid == len(list)-1) or (list[mid] == value and list[mid+1]!=value):
            return mid
        elif list[mid] < value or list[mid+1]==value:
            start = mid+1
        elif list[mid]>value:
            end = mid-1
    return -1
     
print(count([1,1,1,2,3,3,3,4,4,5,5,5,6,6,7,7,7,7,99,99,100,100,100],100))

#Problem 5
def combsort(list):
    gap = len(list)
    shrink = 1.3
    sorted = False
    
    while sorted==False:
        gap = int(gap/shrink)
        if gap>1:
            sorted = False
        else:
            gap = 1
            sorted = True
            
        i = 0
        while i+gap<len(list):
            if distance(list[i])>distance(list[i+gap]):
                temp = list[i]
                list[i] = list[i+gap]
                list[i+gap] = temp
                sorted = False
            i+=1
            
def distance(point):
    return (point[0]**2+point[1]**2)**(1/2)

a =  [[3, 3], [2, 2], [1, 2], [2, 1], [3, 1], [1, 1]]
combsort(a)
print(a)