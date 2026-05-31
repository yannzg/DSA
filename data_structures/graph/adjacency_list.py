# Matrix to Adjency List Conversion

import numpy as np

def matrix_to_list(M):
    """
    Given a matrix M, return an adjacency list AL. 
    Each entry in AL represents the edges associated with each node. 
    The edges are numbered sequentially, starting from 1, and 
    each entry in AL contains the list of edge numbers connected to the corresponding node.
    """
    n,m = np.shape(M) 
    AL = [] 
    for i in range(n):
        L = []
        for j in range(m):
            if M[i, j] == 1:
                L.append(j + 1)
        AL.append(L)

    return AL
    
    
if __name__ == "__main__":
    M = np.array([[0, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0]])
    print(matrix_to_list(M))
            






