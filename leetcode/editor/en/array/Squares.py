# square the array and sort it
def squares(arr):
    l = 0
    r = len(arr) - 1
    res = []
    while l <= r:
        if abs(arr[l]) >= abs(arr[r]):
            res.append(arr[l] * arr[l])
            l += 1
        else:
            res.append(arr[r] * arr[r])
            r -= 1
    return res[-1:None:-1]  # synonymous with res[::-1]


print(squares([-7, -3, 2, 3, 11]))
