#!/usr/bin/python3
"""N Queens problem solver"""


import sys


def solve_nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Raises:
        ValueError: If N is not an integer or is less than 4.

    Returns:
        list: A list of all possible solutions to the N Queens problem.
    """
    if not isinstance(N, int):
        raise ValueError("N must be a number")

    if N < 4:
        raise ValueError("N must be at least 4")

    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at a given position on the board.

        Args:
            board (list): The current state of the chessboard.
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col or \
                    board[i] + i == col + row or \
                    board[i] - i == col - row:
                return False

        return True

    def solve(board, row, solutions):
        """
        Recursive function to solve the N Queens problem.

        Args:
            board (list): The current state of the chessboard.
            row (int): The row index to start placing the queens.
            solutions (list): A list to store the solutions.

        Returns:
            list: A list of all possible solutions to the N Queens problem.
        """
        if row == N:
            # All queens have been placed, add the solution to the result
            solution = []
            for i in range(N):
                queen_pos = [i, board[i]]
                solution.append(queen_pos)
            solutions.append(solution)
            return solutions

        for col in range(N):
            if is_safe(board, row, col):
                # Place a queen at the current position
                board[row] = col

                # Recursively solve the subproblem for the next row
                solutions = solve(board, row + 1, solutions)

        return solutions

    # Initialize an empty chessboard
    board = [-1] * N

    # Solve the N Queens problem
    solutions = solve(board, 0, [])

    # Print the solutions
    for solution in solutions:
        print(solution)

    return solutions


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
