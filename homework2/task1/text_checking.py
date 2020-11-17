"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from typing import List


def get_longest_diverse_words(file_name: str) -> List[str]:
    output_list = []
    punctuation = """!?.,"'"<>«»:;{}[]()#$%^&*-+=/`~"""
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                translator = str.maketrans("", "", punctuation)
                word = word.translate(translator)
                len_unique_symbols = len(set(word))
                if len(output_list) != 10 and word not in output_list:
                    output_list.append(word)
                    output_list.sort(key=lambda x: len(set(x)))
                else:
                    if (
                        len_unique_symbols > len(set(output_list[0]))
                        and word not in output_list
                    ):
                        output_list.append(word)
                        output_list.pop(0)
                        output_list.sort(key=lambda x: len(set(x)))
    return output_list


def get_rarest_char(file_name: str) -> str:
    chars_dict = defaultdict(int)
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    chars_dict[char] += 1

    return min(chars_dict, key=chars_dict.get)


def count_punctuation_chars(file_name: str) -> int:
    punctuation = """!?.,"'"<>«»:;{}[]()#$%^&*-+=/`~"""
    counter = 0
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if char in punctuation:
                        counter += 1
    return counter


def count_non_ascii_chars(file_name: str) -> int:
    ascii_num_set = list(range(128))
    counter = 0
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if not ord(char) in ascii_num_set:
                        counter += 1
    return counter


def get_most_common_non_ascii_char(file_name: str) -> str:
    non_ascii_dict = defaultdict(int)
    ascii_num_set = list(range(128))
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if not ord(char) in ascii_num_set:
                        non_ascii_dict[char] += 1
    return max(non_ascii_dict, key=non_ascii_dict.get)
