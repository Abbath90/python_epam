import pathlib

import pytest

from homework4.task1.read_numbers import read_magic_number


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("1.0", True),
        ("1", True),
        ("3", False),
    ],
)
def test_read_numbers(data: str, expected_result: bool):
    path_to_file = pathlib.Path("temp/")
    file_name = "temp.txt"
    filepath = path_to_file / file_name
    with filepath.open("w", encoding="utf-8") as f:
        f.write(data)
    actual_result = read_magic_number(filepath)
    filepath.unlink()
    assert actual_result == expected_result


@pytest.mark.parametrize("data", ["Seven"])
def test_read_numbers_not_valid_value(data: str):
    path_to_file = pathlib.Path("temp/")
    file_name = "temp.txt"
    filepath = path_to_file / file_name
    with filepath.open("w", encoding="utf-8") as f:
        f.write(data)
        with pytest.raises(ValueError, match="Must be a number"):
            read_magic_number(filepath)
    filepath.unlink()


def test_read_numbers_file_doesnot_exists():
    with pytest.raises(FileNotFoundError, match="File does not exist"):
        read_magic_number(pathlib.Path("random_path"))
