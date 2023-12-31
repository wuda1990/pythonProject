# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            i = i + 1

    # Swap the pivot element with
    # the greater element specified by i
    (array[i], array[high]) = (array[high], array[i])

    # Return the position from where partition is done
    return i


# Function to find the partition position
def partitionLeftPivotal(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[low]

    # Pointer for greater element
    i = high

    # Traverse through all elements
    # compare each element with pivot
    for j in range(high, low, -1):
        if array[j] >= pivot:
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i - 1

    # Swap the pivot element with
    # the greater element specified by i
    (array[i], array[low]) = (array[low], array[i])

    # Return the position from where partition is done
    return i


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        # pi = partition(array, low, high)
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5, 4, 3, 2]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")

# This code is contributed by Adnan Aliakbar
