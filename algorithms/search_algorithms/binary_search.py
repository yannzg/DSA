# Implementation of Binary Search Algorithm

def binary_search(L, x):
    """Given a sorted list L and a value x, find the index of x in the list L."""
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 7, 10, 12, 37, 42, 99]
    x = 37
    print(binary_search(L, x))

    

