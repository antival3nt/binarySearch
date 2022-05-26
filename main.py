# Binary search script

import random
import time

# naive search: scan entire list and ask if it's equal to the target
# if yes, return the index
# if no, return -1
from random import Random, random


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

if __name__ == "__main__":
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # Build sorted list of 10k
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(Random.randint(-3 * length, 3 * length))
    sorted_list = list(sorted_list)

    # Run naive search on sorted list 10.000 times
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search: ", end - start/length, "seconds")

    # Run binary search on sorted list 10.000 times
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search: ", end - start/length, "seconds")