

arr = [1, 2, 3, 4, 5]

second_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def counter(arr):
    total = 0

    for thing in arr:
        total += 1

    return total

def duplicate(arr):
    copy_arr = []

    for thing in arr:
        copy_arr.append(thing)
    
    return copy_arr

def times_table(n):
    times_table = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        times_table.append(row)

    return times_table


    
