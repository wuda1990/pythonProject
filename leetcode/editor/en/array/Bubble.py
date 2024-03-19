def bubble_sort(arr, low, high):
    for i in range(low, high):
        for j in range(low, high - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr


def bubble(arr):
    return bubble_sort(arr, 0, len(arr))


print(bubble([3, 6, 3, 4, 1, 6, 4]))
