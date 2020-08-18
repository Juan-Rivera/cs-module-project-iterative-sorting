def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    # for thing in arr:
    #     if thing == target:
    #         return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    
    return -1  # not found
