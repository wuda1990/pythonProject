def partition(array, low, high):
    pivotal = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivotal:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1],)
    return i + 1


def quick_sort(array, low, high):
    if low >= high:
        return
    p = partition(array, low, high)
    quick_sort(array, low, p - 1)
    quick_sort(array, p + 1, high)


arr = [3, 9, 7, 2, 5, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
