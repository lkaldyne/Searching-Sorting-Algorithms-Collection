def binsearch(val,alist):
    found = False
    first = 0
    last = len(alist)-1
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == val:
            found = True
        else:
            if alist[midpoint] > val:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


print binsearch(16,sorted([8,4,6,2,5,3,5,3,76,7,3,45]))