def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        swap = False
        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                swap = True
        # if there is no swap, then whole array is sorted
        if not swap:
            break
    return arr


print(bubble_sort([3, 9, 7, 2, 5, 4]))
