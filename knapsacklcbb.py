class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

    def __repr__(self):
        return f"Item({self.profit}, {self.weight})"


def knapsack_01(items, capacity):
    """
    Solve the knapsack problem using least cost branch and bound.

    Args:
        items (list): List of items with their profits and weights.
        capacity (int): Maximum weight capacity of the knapsack.

    Returns:
        Tuple: The maximum profit and the items to include in the knapsack.
    """
    # Initialize the variables to store the best solution and profit
    best_solution = []
    best_profit = 0

    def knapsack_util(profit, weight, level, solution):
        """
        Recursive helper function to solve the knapsack problem.

        Args:
            profit (int): Current profit.
            weight (int): Current weight.
            level (int): Current item level.
            solution (list): Current solution.

        Returns:
            None
        """
        # Access the variables from the outer scope
        nonlocal best_profit
        nonlocal best_solution

        # Check if the current solution is better than the best solution found so far
        if weight <= capacity and profit > best_profit:
            best_profit = profit
            best_solution = solution.copy()

        # Base case: reached the end of the items list
        if level == len(items):
            return

        # Check if the current item can be included in the knapsack
        item = items[level]
        if weight + item.weight <= capacity:
            solution.append(item)
            # Recursive call to explore the next level
            knapsack_util(
                profit + item.profit, weight + item.weight, level + 1, solution
            )
            solution.pop()

        # Recursive call to explore the next level without including the current item
        knapsack_util(profit, weight, level + 1, solution)

    # Call the helper function to solve the knapsack problem
    knapsack_util(0, 0, 0, [])

    # Return the best profit and solution found
    return best_profit, best_solution


if __name__ == "__main__":
    # Example usage
    # items = [Item(10, 2), Item(20, 5), Item(30, 10), Item(40, 12)]
    w = [3, 4, 6, 5]
    p = [2, 3, 1, 4]
    items = [Item(p[i], w[i]) for i in range(len(p))]

    best_profit, best_solution = knapsack_01(items, 8)
    print("Best solution:")
    print("Total profit:", best_profit)
    print("Items selected:", best_solution)
