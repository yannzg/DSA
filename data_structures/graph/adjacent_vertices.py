# Find all the adjacent vertices of a vertex in a graph represented by 
# - an adjacency matrix 
# - an adjacency list

import numpy as np

def matrix_adjacent_vertices(M, u):
    """
    Given an adjacency matrix M, and a vertex u, 
    return a list containing all vertices that are directly connected to u.

    Vertex u corresponds to the number of the vertex.
    """
    L = []
    n = np.shape(M)[0]

    for j in range(n):
        if M[u - 1, j] > 0:
            L.append(j + 1)

    return L


def list_adjacent_vertices(L, v):
    """
    Given an adjacency list L, and a vertex v, 
    return a list containing all vertices that are directly connected to v.

    Vertex v corresponds to the number of the vertex.
    """
    index = v - 1

    if index < 0 or index > len(L):
        raise ValueError(f"Vertex {v} is out of range. {v} should be between 1 and {len(L)}")

    return L[index]


if __name__ == "__main__":
    M = np.array([[0, 1, 1, 1, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 0, 1, 0, 0]])
    u = 3
    print(f"\nFor matrix \n {M}, \n\t the adjacent vertices of {u} are {matrix_adjacent_vertices(M, u)}.\n\n")

    L = [[2, 3, 4], [1, 3, 5], [1, 2, 4], [1, 3], [2]]
    v = 2
    print(f"According to adjacency list {L}, the adjacent vertices of {v} are {list_adjacent_vertices(L, v)}.\n")







