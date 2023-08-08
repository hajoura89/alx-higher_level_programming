#!/usr/bin/python3
"""Solves the N-queens puzzle"""
import sys


def init_board(n):
    """Initialize a chessboard with 0"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def deepcopy(board):
    """Deepcopy of a chessboard"""
    if isinstance(board, list):
        return list(map(deepcopy, board))
    return (board)


def solve(board):
    """lists representation of a solved chessboard"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def x_out(board, row, col):
    """x_out spots on a chessboard
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # x_out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # x_out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # x_out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # x_out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # x_out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x_out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # x_out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x_out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def rec_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(solve(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = deepcopy(board)
            tmp_board[row][c] = "Q"
            x_out(tmp_board, row, c)
            solutions = rec_solve(tmp_board, row + 1,
                                  queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = rec_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
