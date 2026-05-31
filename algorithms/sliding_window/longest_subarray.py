# Find the longest subarray with sum less than S

def longest_subarray(arr, s):

    left = 0
    curr = 0
    best = 0

    for r in range(len(arr)):
        curr += arr[r]

        while curr >= s:
            curr -= arr[left]
            left += 1
            
        
        best = max(best, r - left + 1)

    return best



if __name__ == "__main__":
    arr = [2, 3, 6, 1, 2, 10, 3, 16, 33, 43, 43]
    print(longest_subarray(arr, 20))

