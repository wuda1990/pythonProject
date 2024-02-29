def minimum_sub_array_sum(arr, target):
    i = 0
    sum = 0
    min_length = float('inf')
    for j in range(len(arr)):
        sum += arr[j]
        while sum >= target:
            min_length = min(min_length, j - i + 1)
            sum -= arr[i]
            i += 1
    if min_length == float('inf'):
        return 0
    return min_length


print(minimum_sub_array_sum([2, 3, 1, 2, 4, 3], 7))
print(minimum_sub_array_sum([1, 4, 4], 4))
