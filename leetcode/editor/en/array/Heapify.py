def heapify(arr, N, i):
    lc = 2 * i + 1
    rc = 2 * i + 2
    maximum = i
    if lc < N and arr[lc] > arr[maximum]:
        maximum = lc
    if rc < N and arr[rc] > arr[maximum]:
        maximum = rc
    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, N, maximum)


def heap_sort(arr):
    length = len(arr)
    mid = (length - 2) // 2
    for i in range(mid, -1, -1):
        heapify(arr, length, i)
    for i in range(length - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


print(heap_sort([8, 3, 4, 7, 1]))
print(heap_sort([3, 9, 7, 2, 5, 4]))
