# 谢尔排序，时间复杂度约为O(n^3/2)
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startpostion in range(sublistcount):
            gapInsertionSort(alist, startpostion, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shellSort(alist)
print(alist)