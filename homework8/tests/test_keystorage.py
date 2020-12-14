import os
import tempfile

import pytest

from homework8.task1.key_storage import KeyStorage


class TestFileContent:
    def __init__(self, content):

        self.file = tempfile.NamedTemporaryFile(mode="w", delete=False)

        with self.file as f:
            f.write(content)

    @property
    def filename(self):
        return self.file.name

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        os.unlink(self.filename)


def test_keystorage_len(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        assert len(key_storage) == 3


def test_keystorage_len(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        assert len(key_storage) == 3


def test_keystorage_as_collection(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        assert key_storage["name"] == "kek"


def test_keystorage_has_attributes(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        assert key_storage.name == "kek"


def test_keystorage_contains(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        assert "name" in key_storage


def test_keystorage_add_item(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        key_storage["atr1"] = 666
        key_storage.atr2 = 777
        assert "atr1" in key_storage and "atr2" in key_storage


def test_keystorage_add_int_item(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        with pytest.raises(ValueError, match="Invalid key"):
            key_storage["1"] = "hey"


def test_keystorage_del_item(content="name=kek\n last_name=top\n power=9001"):
    with TestFileContent(content) as test_file:
        key_storage = KeyStorage(test_file.filename)
        del key_storage["name"]

        assert len(key_storage) == 2
