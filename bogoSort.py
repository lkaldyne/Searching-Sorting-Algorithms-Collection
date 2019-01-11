from random import randint
iterationCount = 0
def isSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
def bogoSort(arr):
    global iterationCount
    arrLen = len(arr)
    while not isSorted(arr):
        firstSpot = randint(0,arrLen-1)
        secondSpot = randint(0,arrLen-1)
        temp = arr[firstSpot]
        arr[firstSpot] = arr[secondSpot]
        arr[secondSpot] = temp
        iterationCount += 1
        print("not done yet! Iteration :" + str(iterationCount))
    return arr

testList = [1,4,2,3,18]
print (bogoSort(testList))