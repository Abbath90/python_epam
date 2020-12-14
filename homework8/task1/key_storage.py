"""Homework 1:
We have a file that works as key-value storage, each like is represented as key
and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both as a number
and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible
as collection items and as attributes. Example: storage['name'] # will be string
'kek' storage.song_name # will be 'shadilay' storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence. In case when
value cannot be assigned to an attribute (for example when there's a line 1=something)
ValueError should be raised. File size is expected to be small, you are permitted
to read it entirely into mem"""


class KeyStorage:
    def __init__(self, path_to_file):
        storage_object = self.create_storage_object(path_to_file)
        for name in storage_object:
            setattr(self, name, storage_object[name])

    @classmethod
    def create_storage_object(self, path_to_file):
        list_of_data = []
        with open(path_to_file) as f:
            for line in f.readlines():
                list_of_data.append(line.rstrip().split("="))
        return {k: int(v) if v.isdigit() else v for k, v in dict(list_of_data).items()}

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __contains__(self, key):
        return key in self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if isinstance(key, (int, float)) or key.isdigit():
            raise ValueError("Invalid key")
        else:
            self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]
