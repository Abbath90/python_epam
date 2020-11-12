"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import Dict, List, Tuple


def get_longest_diverse_words(file_name: str) -> List[str]:
    output_list = []
    words_dict = {}
    punctuation = """!?.,"'"<>«»:;{}[]()#$%^&*-+=/`~"""
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                translator = str.maketrans("", "", punctuation)
                word = word.translate(translator)
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
    for word in words_dict:
        if len(word) == len(set(word)):
            output_list.append(word)
    output_list.sort(key=len)
    return output_list[-10:]


def get_rarest_char(file_name: str) -> str:
    chars_dict = {}
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if char in chars_dict:
                        chars_dict[char] += 1
                    else:
                        chars_dict[char] = 1

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
    non_ascii_dict = {}
    ascii_num_set = list(range(128))
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if char in non_ascii_dict and not ord(char) in ascii_num_set:
                        non_ascii_dict[char] += 1
                    elif char not in non_ascii_dict and not ord(char) in ascii_num_set:
                        non_ascii_dict[char] = 1
    return max(non_ascii_dict, key=non_ascii_dict.get)
