# Implementation of Linear Search Algorithm

def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [23, 2, 5, 99, 340, 734, 200, 456, 789, 123, 456, 789, 1000]
    target = 123
    result = linear_search(arr, target)
    print(f"Element {target} found at index {result}")


