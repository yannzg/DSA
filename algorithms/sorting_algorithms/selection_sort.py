# Implementation of Selection Sort

def selection_sort(L):
    n = len(L)

    for i in range(n):
        min_index = i 

        for j in range(i+1, n):
            if L[j] < L[min_index]:
                min_index = j

        temp = L[i]
        L[i] = L[min_index]
        L[min_index] = temp
    
    return L


if __name__ == "__main__":
    L = [11, 21, 1, 7, 33, 2, 21, 99, 102]
    print(selection_sort(L))