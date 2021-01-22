"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
#>>> universal_file_counter(test_dir, "txt")
6
#>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import glob
import os
from pathlib import Path
from typing import Callable, Optional, TextIO


def tokenizer_generator(
    file_handler: TextIO, tok: Optional[Callable]
) -> Generator[int, None, None]:
    buffer = ""
    char = " "
    while True:
        char = file_handler.read(1)
        if not char:
            yield 1  # buffer
            break
        buffer += char

        if len(tok(buffer)) == 1:
            continue
        else:
            yield 1  # tok(buffer)[0]
            buffer = tok(buffer)[1]


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for file in Path(dir_path).glob("*." + file_extension):
        with open(file) as f:
            if tokenizer is not None:
                for token in tokenizer_generator(f, tokenizer):
                    counter += token
            else:
                counter += sum(1 for _ in f)

    return counter
