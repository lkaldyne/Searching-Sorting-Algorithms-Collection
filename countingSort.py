from random import randint

def countingSort(arr):
    lBound = min(arr)
    uBound = max(arr)
    buckets = {}
    sortedList = [0] * len(arr)
    for elem in arr:
        if elem in buckets:
            buckets[elem] += 1
        else:
            buckets[elem] = 1
    sortedPlaceholder = 0
    for i in range(lBound,uBound+1):
        if i in buckets:
            for n in range(buckets[i]):
                sortedList[sortedPlaceholder] = i
                sortedPlaceholder += 1
    return sortedList

thing = [0] * 1000000
for k in range(1000000):
    thing[k] = randint(0,1000000)

print (countingSort(thing))
