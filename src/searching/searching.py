def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    min = 0
    max = len(arr - 1)

    while (min + max) //2:
        i = (min + max) //2

        if arr[i] == target:
            return i
        elif target < arr[i]:
            max = i
        else:
            min = i + 1

    return -1  # not found
