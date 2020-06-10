import math

def inHalf(a, converger):
        # First half of the array is b
        b = a[:int((len(a)/2))]
        # Second half of the array is c
        c = a[int((len(a)/2)):]
        # Base case when we kept dividing until there were single-value arrays:
        if len(b) == 1 and len(c) == 1:
            # Converge the numbers of the two single-value arrays into one sorted array that I put into converger array:
            if b[0] < c[0]:
                converger.append([b[0],c[0]])
                return
            else:
                converger.append([c[0],b[0]])
                return
        # Base case when when we kept dividing until we got to the point of one single-value array and one two-value array:
        if len(b) == 1 and len(c) == 2:
            # First sort the two-value array:
            if c[0] < c[1]:
                c = [c[0],c[1]]
            else:
                c = [c[1],c[0]]
            # Converge the three numbers into one sorted array that I put into converger array:
            if c[0] > b[0]:
                converger.append([b[0],c[0],c[1]])
                return
            else:
                if c[1] > b[0]:
                    converger.append([c[0],b[0],c[1]])
                    return
                else:
                    converger.append([c[0],c[1],b[0]])
                    return
        return [inHalf(b,converger),inHalf(c,converger)]

def twoArraysIntoOneFunc(arr1, arr2):
    convergedArr = []
    j = 0
    for i in range(len(arr1)):
        if j > (len(arr2)-1):
            convergedArr.append(arr1[i])
            continue
        while arr1[i] >= arr2[j]:
            convergedArr.append(arr2[j])
            if j != (len(arr2)-1):
                j += 1
            else:
                j +=1
                break
        convergedArr.append(arr1[i])
        while i == (len(arr1)-1) and j != (len(arr2)):
            convergedArr.append(arr2[j])
            j += 1
    return convergedArr

def recurringConvergingFunc(array):
    if len(array) == 1:
        return array
    i = 0
    while i < (len(array)-1):
        convergedArray = twoArraysIntoOneFunc(array[i],array[i+1])
        array[i] = convergedArray
        array.remove(array[i+1])
        i += 1
    return recurringConvergingFunc(array)

def sort(a):
    converger = []
    inHalf(a, converger)
    return recurringConvergingFunc(converger)
    
# A little bit of interaction with the user:
print("\n")
print("Hi, please type in numbers you want to sort divided just by comma (i.e.: 4,15,1,70,2):"+"\n")
arrayToSort = input().split(",")
result = []
for num in arrayToSort:
    result.append(int(num))
print(sort(result)[0])