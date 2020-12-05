from typing import List

import pytest

from homework7.task3.tictac import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["-", "-", "x"], ["-", "x", "o"], ["x", "o", "x"]], "x wins!"),
        ([["o", "o", "x"], ["-", "o", "x"], ["x", "-", "o"]], "o wins!"),
        ([["-", "x", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
        ([["x", "x", "o"], ["o", "o", "x"], ["x", "o", "x"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result
