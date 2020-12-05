"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    win_lines = [["x", "x", "x"], ["o", "o", "o"]]
    columns = [column for column in board]
    rows = [list(row) for row in list(zip(*board))]
    diag = [column[i] for i, column in enumerate(board)]
    side_diag = [column[-1 - i] for i, column in enumerate(board)]
    diags = [diag, side_diag]
    lines = columns + rows + diags

    if win_lines[0] in lines:
        return "x wins!"
    elif win_lines[1] in lines:
        return "o wins!"
    elif any("-" in line for line in lines):
        return "unfinished!"
    else:
        return "draw!"
