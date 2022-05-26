# Binary search script

# naive search: scan entire list and ask if it's equal to the target
# if yes, return the index
# if no, return -1
def naive_search(l, target):
    # Example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search uses divide and conquer
# we will leverage the fact that our list is sorted
def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
