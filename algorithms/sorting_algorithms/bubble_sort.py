# Implementation of Bubble Sort


def bubble_sort(L):
    n = len(L)

    for i in range(n):

        for j in range(n-i-1):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

    return L



if __name__ == "__main__":
    L = [11, 21, 1, 7, 33, 2, 21, 99, 102]
    print(bubble_sort(L))