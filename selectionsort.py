def selectionsort(numlist):
    for i in range(len(numlist)):
        smallestspot = i
        for j in range(i+1,len(numlist)):
            if numlist[j] < numlist[smallestspot]:
                smallestspot = j
        if i != smallestspot:
            numlist[smallestspot],numlist[i] = numlist[i],numlist[smallestspot]
    return numlist

print selectionsort([8,4,6,2,5,3,5,3,76,7,3,45])


