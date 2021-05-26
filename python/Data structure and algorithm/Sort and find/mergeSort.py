# 归并算法的过程非为分裂和归并，分裂的过程类似于二分查找为对数复杂度，时间复杂度为O(log n),
# 归并的过程为线性复杂度，时间复杂度为O(n)
# 所以归并算法总的时间复杂度为O(nlon n)
# 归并算法使用了额外一倍的存储空间，在特大数据集进行排序的时候需考虑
def mergeSort(alist):
## print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = lefthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
## print("Merging", alist)


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
mergeSort(alist)
print(alist)


# merge sort
def merge_sort(lst):
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，并递归调用
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])  # 左半部排好序
    right = merge_sort(lst[middle:])  # 右半部排好序

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
merge_sort(alist)
print(alist)
