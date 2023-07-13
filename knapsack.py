import numpy as np


class Item:
    def __init__(self, profit: int, weight: int):
        self.profit = profit
        self.weight = weight

    def __repr__(self):
        return f"Item({self.profit}, {self.weight})"


def knapsack_01(items: list[Item], capacity: int) -> np.ndarray:
    """
    This function solves the 0/1 knapsack problem using dynamic programming.
    Given a set of items, each with a value and weight, and a maximum weight capacity,
    it determines the maximum value subset of items that fit into the knapsack.

    Parameters
    ----------
    items : list[Item]
        List of Item objects representing the items
    capacity : int
        Integer representing the maximum weight capacity of the knapsack

    Returns
    -------
    numpy.ndarray
        NumPy array of floats representing the dynamic programming table used to solve the problem
    """
    # Get the number of items
    n = len(items)

    # Initialize the dynamic programming table with zeros
    table = np.zeros((n + 1, capacity + 1), dtype=int)
    selected_items = []
    # Fill the dynamic programming table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the weight of the current item is less than or equal to w,
            # we can either include it or exclude it from the knapsack
            if items[i - 1].weight <= w:
                # Choose the maximum value between including the item and excluding it
                table[i, w] = max(
                    table[i - 1, w],
                    items[i - 1].profit + table[i - 1, w - items[i - 1].weight],
                )
            # If the weight of the current item is greater than w,
            # we cannot include it in the knapsack
            else:
                table[i, w] = table[i - 1, w]

    # Retrieve the list of selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w >= 0:
        # If the current item was included, add it to the list of selected items
        if table[i, w] != table[i - 1, w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1].weight
        i -= 1
    # Return the dynamic programming table
    return table[n][capacity], sorted(selected_items, key=lambda x: x.weight)


if __name__ == "__main__":
    w = [3, 4, 6, 5]
    p = [2, 3, 1, 4]
    items = [Item(p[i], w[i]) for i in range(len(p))]
    best_profit, best_solution = knapsack_01(items, 8)
    print("Best solution:")
    print("Total profit:", best_profit)
    print("Items selected:", best_solution)
