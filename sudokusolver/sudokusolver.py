import numpy as np
import random


# =========================
# SUDOKU GENERATOR
# =========================

def is_valid(board, row, col, number):
    # Check row
    if number in board[row]:
        return False

    # Check column
    if number in board[:, col]:
        return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    box = board[box_row:box_row + 3, box_col:box_col + 3]

    if number in box:
        return False

    return True


def fill_board(board):
    """
    Fill an empty board with a valid Sudoku solution.
    Uses backtracking.
    """

    for row in range(9):
        for col in range(9):

            if board[row, col] == 0:

                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for number in numbers:

                    if is_valid(board, row, col, number):

                        board[row, col] = number

                        if fill_board(board):
                            return True

                        board[row, col] = 0

                return False

    return True


def generate_sudoku():
    """
    Generate a complete valid Sudoku board,
    then remove numbers to create a puzzle.
    """

    board = np.zeros((9, 9), dtype=int)

    fill_board(board)

    # Remove numbers to create the puzzle
    puzzle = board.copy()

    cells_to_remove = 45

    positions = [
        (row, col)
        for row in range(9)
        for col in range(9)
    ]

    random.shuffle(positions)

    for row, col in positions[:cells_to_remove]:
        puzzle[row, col] = 0

    return puzzle, board


# =========================
# SUDOKU SOLVER
# =========================

def solve_puzzle(board):
    """
    Solve a Sudoku puzzle using backtracking.
    """

    for row in range(9):
        for col in range(9):

            if board[row, col] == 0:

                for number in range(1, 10):

                    if is_valid(board, row, col, number):

                        board[row, col] = number

                        if solve_puzzle(board):
                            return True

                        # Undo the decision
                        board[row, col] = 0

                return False

    return True


# =========================
# PROGRAM
# =========================

puzzle, solution = generate_sudoku()

print("Generated Puzzle:")
print(puzzle)

print("\nOriginal Solution:")
print(solution)

solved_board = puzzle.copy()

solve_puzzle(solved_board)

print("\nSolver Result:")
print(solved_board)