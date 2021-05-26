# 二分查找，算法复杂度o（log n）
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if not found:
        midpoint = None
    else:
        midpoint = midpoint + 1
    return found, midpoint


testlist = [0, 1, 2, 8, 13, 17, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

def RebinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True, midpoint + 1
        else:
            if item < alist[midpoint]:
                return RebinarySearch(alist[:midpoint], item)
            else:
                return RebinarySearch(alist[midpoint + 1:], item)


print(RebinarySearch(testlist, 3))
print(RebinarySearch(testlist, 13))