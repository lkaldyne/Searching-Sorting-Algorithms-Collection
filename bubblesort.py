def bubblesort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    return alist

print bubblesort([8,4,6,2,5,3,5,3,76,7,3,45])