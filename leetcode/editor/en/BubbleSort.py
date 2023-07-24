def bubbleSort(array, low, high):
    for i in range(low, high):
        for j in range(low, low + high - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5, 4, 3, 2]
    print(bubbleSort(array, 2, len(array) - 1))
