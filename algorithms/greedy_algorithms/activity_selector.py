# Implementation of the Activity Selection Problem
# Also known as Interval Scheduling Maximization Problem

I = [[7, 9], [8, 9], [8, 10], [8, 11], [7, 12], [10, 12]]

def is_available(T, n):
    """
    Check for the first available room at or before time n.
    
    Args:
        T (list of int): Times when each room becomes available.
        n (int): Time when the next room starts.

    Returns: 
        int: Number (index) of the room available for the activity starting at n if available.
    """
    for k in range(len(T)):
        if n >= T[k]:
            return k
    return -1

T = [13, 12, 11]  # Heures de fin des cours pour 3 salles
n = 12         # Heure de début du prochain cours


print(is_available(T, n))