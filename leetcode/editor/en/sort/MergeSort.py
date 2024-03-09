def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return
    m = length // 2
    L = arr[0:m]
    R = arr[m:]
    merge_sort(L)
    merge_sort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k = k + 1
    while i < len(L):
        arr[k] = L[i]
        i = i + 1
        k = k + 1
    while j < len(R):
        arr[k] = R[j]
        j = j + 1
        k = k + 1
    return arr


print(merge_sort([12, 11, 13, 5, 6, 7]))
