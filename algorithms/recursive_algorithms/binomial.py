# Recursive call with memoization

def binomial(n, k, memo={}):
    if k > n: 
        return 0 
    elif k == 0 or k == n:
        return 1
    
    if (n, k) in memo:
        return memo[(n, k)]
    
    memo[(n, k)] = binomial(n-1, k-1, memo) + binomial(n-1, k, memo)   
    return memo[(n, k)] 

if __name__ == "__main__":
    print(binomial(10, 4))