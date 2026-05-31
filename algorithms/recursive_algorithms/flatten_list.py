# Flatten a list of integers & lists 

def flatten(L):

    result = []

    for item in L:

        if isinstance(item, int):
            result.append(item)

        else:
            result.extend(flatten(item))
    
    return result


if __name__ == "__main__":
    L = [4, [2, 12], [[1, 2], 3], [4, 5], [6, 7]]

    print(flatten(L))