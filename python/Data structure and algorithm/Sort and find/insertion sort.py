# 插入排序，最差情况的算法复杂度与冒泡排序相同为O(n^2),最好情况为O(n)
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
insertionSort(alist)
print(alist)