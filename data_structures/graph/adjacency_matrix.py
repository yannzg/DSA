# Adjency List to Matrix Conversion

import numpy as np

def list_to_matrix(AL):
    """
    Given an adjacency list AL, return a matrix M.
    Each entry in AL represents the nodes connected to the corresponding node in the matrix.
    Each entry contains the list of nodes that have an edge with the corresponding node.
    """
    n = len(AL)
    M = np.zeros((n, n))

    for i in range(n):
        L = AL[i]
        for j in range(n):
            for x in L:
                M[i, x - 1] = 1
            M[i, j] = 0
    
    return M

if __name__ == "__main__":
    AL = [[2, 3, 4], [1, 3, 5], [1, 2, 4], [1, 3], [2]]
    print(list_to_matrix(AL))

    