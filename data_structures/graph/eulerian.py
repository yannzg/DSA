import numpy as np

def eulerien(M):
    """
    Given the matrix M of a connected graph, return True if the graph is Eulerian and False otherwise.

    A graph is Eulerien if it is an Eulerian cycle. 
    To be an Eulerian cycle, every vertex in the graph must have an even degree.
    """
    n, m = np.shape(M)

    for i in range(n):
        line_sum = 0
        for j in range(m):
            line_sum += M[i, j]
        if line_sum % 2 != 0:
            return False
        
    return True

M = np.array([[0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [1, 1, 1, 1, 0]])
print(eulerien(M))





