class QuickSort(object):

    def partition(self, arr, low, high):
        pivotal = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivotal:
                (arr[i], arr[j]) = (arr[j], arr[i])
                i = i + 1
        (arr[i], arr[high]) = (arr[high], arr[i])
        return i

    def quickSort(self, arr, low, high):
        if low >= high:
            return
        p = self.partition(arr, low, high)
        self.quickSort(arr, low, p - 1)
        self.quickSort(arr, p + 1, high)


# Driver code
if __name__ == '__main__':
    array = [8, 3, 40, 7, 91, 32]
    N = len(array)

    # Function call
    solution = QuickSort()
    solution.quickSort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")
