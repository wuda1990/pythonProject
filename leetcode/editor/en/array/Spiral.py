def spiral(n):
    arr = [[0] * n for _ in range(n)]
    i, j = 0, 0
    di, dj = 0, 1
    for k in range(n * n):
        arr[i][j] = k + 1
        if arr[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return arr


print(spiral(3))
print(spiral(4))
print(spiral(5))
