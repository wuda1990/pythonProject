# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


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
        pi = partition(array, low, high)
        # pi = partitionLeftPivotal(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
    array = [8,3,40,7,91,32]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")

# This code is contributed by Adnan Aliakbar
