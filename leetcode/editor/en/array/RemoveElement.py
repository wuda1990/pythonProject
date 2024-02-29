def remove_element(arr, x):
    i = 0
    for j in range(0, len(arr)):
        if arr[j] != x:
            arr[i] = arr[j]
            i += 1
    return arr


print(remove_element([3, 5, 6, 2, 5, 8, 3], 5))
print(remove_element([3, 2, 2, 3], 3))
