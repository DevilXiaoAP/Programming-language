# 顺序查找，无序表查找,算法复杂度o(n)
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    if not found:
        pos = None
    else:
        pos = pos + 1

    return found, pos


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


# 有序表查找代码,算法复杂度o(n)
def orderedSequentialSarch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    if not found:
        pos = None
    else:
        pos = pos + 1
    return found, pos


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 43]
print(orderedSequentialSarch(testlist, 3))
print(orderedSequentialSarch(testlist, 13))
