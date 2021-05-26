# 冒泡排序的时间复杂度为O(n^2),比对的时间也为O(n^2)
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)


# 比对排序在排序方面，比冒泡排序稍优，比对排序的时间复杂度为O(n^2),比对的时间也为O(n^2)
def selectionSort(alist):
    for fillslot in range(len(alist) -1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
selectionSort(alist)
print(alist)
