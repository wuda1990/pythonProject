def heapify(arr, N, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < N and arr[largest] < arr[l]:
        largest = l
    if r < N and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, N, largest)


def heap_sort(arr):
    length = len(arr)
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)
    for i in range(length - 1, -1, -1):
        (arr[0], arr[i]) = (arr[i], arr[0])
        heapify(arr, i, 0)
    return arr


print(heap_sort([3, 9, 7, 2, 5, 4]))
