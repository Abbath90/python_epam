import tempfile
from pathlib import Path

import pytest

from homework9.task3.file_counter import universal_file_counter

content1 = "1\n 2\n 3"
content2 = "4\n 5\n 6"
content3 = "7\n 8\n 9"
content4 = "aa! 333\naa! cvcv!\ndfsdf!rr"
content5 = "!!!aaaaaaaaaaaaaaaaaaaaa"


def test_file_counter_without_tokenizer(tmpdir):
    tmpdir.join("file1.txt").write(content1)
    tmpdir.join("file2.txt").write(content2)
    tmpdir.join("file3.file").write(content3)
    actual_result = universal_file_counter(Path(tmpdir), "txt", None)
    assert actual_result == 6


def test_file_counter_with_tokenizer(tmpdir):
    tmpdir.join("file4.txt").write(content4)
    tmpdir.join("file5.txt").write(content5)

    actual_result = universal_file_counter(
        Path(tmpdir), "txt", lambda string: string.split("!")
    )
    assert actual_result == 9
