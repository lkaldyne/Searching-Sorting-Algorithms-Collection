def insertionsort(numlist):
    for i in range(1,len(numlist)):
        position = i
        value = numlist[i]
        while position > 0 and numlist[position-1] > value:
            numlist[position] = numlist[position-1]
            position = position - 1
        numlist[position] = value
    return numlist

print insertionsort([8,4,6,2,5,3,5,3,76,7,3,45])
