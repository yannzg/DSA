# Implementation of the Change-Making Problem

def change_making(price, money):
    """
    Calculate the minimum number of coins needed to give change.

    Args: 
        price (int): Price of the item
        money (int): Amount of money given


    Returns: 
        list: A list P of coin values that sum up to the change required.
    """
    change = money - price
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    coins.reverse()  # Starting with the largest coin. 
    P = []

    i = 0
    if price == money:
        return [0]

    while change > 0:
        if i > len(coins):
            break
        elif change >= coins[i]:
            P.append(coins[i])
            change -= coins[i]
        else:
            i += 1  # Moving to the smaller coin

    return P


def main():
    price = 337
    money = 500
    change = change_making(price, money)
    print("Change to be returned: ", change)

if __name__ == "__main__":
    main()