def solve_n_queens(n):
    """
    Generate the solutions to the N-Queens problem.

    Parameters:
    - n (int): The size of the chessboard and the number of queens to place.

    Returns:
    - list: A list of lists representing the distinct solutions to the N-Queens problem. Each inner list represents a solution, where each element is the column position of a queen in a specific row.
    """

    # Check if it's safe to place a queen at the given position on the board.
    def is_safe(board, row, col):
        """
        Check if it is safe to place a queen on a chessboard at the given position.

        Parameters:
        - board (list): The current state of the chessboard represented as a list of integers, where each integer represents the column position of a queen in a specific row.
        - row (int): The row position where we want to place a queen.
        - col (int): The column position where we want to place a queen.

        Returns:
        - bool: True if it is safe to place a queen at the given position, False otherwise.
        """
        # Check if there is a queen in the same column or diagonal
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    # Backtracking function to find all distinct solutions.
    def backtrack(board, row, solutions):
        """
        Backtracks through the board to find all solutions for the N-Queens problem.

        Parameters:
        - board (list): The current state of the chessboard.
        - row (int): The current row being considered.
        - solutions (list): A list to store the valid solutions.

        Returns:
        - None
        """
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1, solutions)
                board[row] = -1  # Reset the value after backtracking

    board = [-1] * n
    solutions = []

    backtrack(board, 0, solutions)

    return solutions


if __name__ == "__main__":
    print(len(solve_n_queens(8)))
