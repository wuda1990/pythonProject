def partition(arr, low, high):
    pivotal = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivotal:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)
    return arr


def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr


print(sort([3, 6, 2, 8, 3, 8, 3]))
print(sort([3, 9, 7, 2, 5, 4]))
