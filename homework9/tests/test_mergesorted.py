from pathlib import Path

import pytest

from homework9.task1.merge_sorted import merge_sorted_files

content1 = "1\n 2\n 3"
content2 = "4\n 5\n 6"


def test_merge_sorted_files(tmpdir):
    tmpdir.join("file1.txt").write(content1)
    tmpdir.join("file2.txt").write(content2)

    assert list(merge_sorted_files(tmpdir.listdir())) == [1, 2, 3, 4, 5, 6]
