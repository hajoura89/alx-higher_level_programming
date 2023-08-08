#!/usr/bin/python3
"""A program that solves the N queens problem"""
import sys


def init_chessboard(n):
    """Initialize with 0"""
    chessboard = []
    [chessboard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chessboard]
    return (chessboard)


def chessboard_copy(chessboard):
    """Return a deepcopy"""
    if isinstance(chessboard, list):
        return list(map(chessboard_copy, chessboard))
    return (chessboard)


def solution(chessboard):
    """lists representation of a solved chessboard"""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def out(chessboard, row, col):
    """Out spots on a chesschessboard

    Args:
        chessboard (list): The current working chesschessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def solve(chessboard, row, queens, solutions):
    """Solve an N-queens puzzle

    Args:
        chessboard (list): The current working chesschessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(chessboard):
        solutions.append(solution(chessboard))
        return (solutions)

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_chessboard = chessboard_copy(chessboard)
            tmp_chessboard[row][c] = "Q"
            out(tmp_chessboard, row, c)
            solutions = solve(tmp_chessboard, row + 1,
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

    chessboard = init_chessboard(int(sys.argv[1]))
    solutions = solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
