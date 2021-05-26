# 快速排序过程分为两部分，分裂和移动
# 算法复杂度为O(nlog n)
# 且不需要额外的存储空间
# 极端情况，如果有一部分始终没有数据就会退化到O(n^2)，再加上递归调用的开销（比冒泡排序还要糟糕）
# 该算法的关键是中值的选取


def quikeSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quikeSort(alist)
print(alist)
