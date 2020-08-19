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
    # keep track of upper/lower
    low = 0
    high = len(arr)-1
    while low <= high:
        #find middle 
        middle = (low + high) // 2 # the // rounds down

        # check if target is right at the middle
        if target == arr[middle]:
            return middle
        # target is above middle
        elif target > arr[middle]:
            low = middle - 1
        # target is below middle
        elif target < arr[middle]:
            high = middle + 1
    
    return -1  # not found
