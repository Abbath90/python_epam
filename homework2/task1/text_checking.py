"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List, Dict, Tuple


def get_key_by_value(inp_dic: Dict, value: int) -> any:
    for i in inp_dic.items():
        if i[1] == value:
            return i[0]


def text_checking(file_name: str) -> Tuple[List[str], str, int, int, str]:
    chars_dict = {}
    words_dict = {}
    non_ascii_dict = {}
    punctuation = """!?.,"'"<>«»:;{}[]()#$%^&*-+=/`~"""
    ascii_num_set = list(range(128))
    with open(file_name, encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for word in line.lower().rstrip("\n").split(" "):
                for char in word:
                    if char in chars_dict:
                        chars_dict[char] += 1
                        if not ord(char) in ascii_num_set:
                            non_ascii_dict[char] += 1
                    else:
                        chars_dict[char] = 1
                        if not ord(char) in ascii_num_set:
                            non_ascii_dict[char] = 1
                translator = str.maketrans('', '', punctuation)
                word = word.translate(translator)
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1

    longest_diverse_words = get_longest_diverse_words(words_dict)
    rarest_char = get_rarest_char(chars_dict)
    punctuation_chars = count_punctuation_chars(chars_dict)
    non_ascii_chars = count_non_ascii_chars(non_ascii_dict)
    most_common_non_ascii_char = get_most_common_non_ascii_char(non_ascii_dict)

    return (longest_diverse_words, rarest_char, punctuation_chars, non_ascii_chars, most_common_non_ascii_char)


def get_longest_diverse_words(words_dict: Dict[str, str]) -> List[str]:
    output_list = []
    for word in words_dict:
        if len(list(word)) == len(set(word)):
            output_list.append(word)
    output_list.sort(key=len)
    return output_list[-10:]


def get_rarest_char(chars_dict: Dict[str, str]) -> str:
    min_value_in_dict = min(chars_dict.values())

    return get_key_by_value(chars_dict, min_value_in_dict)


def count_punctuation_chars(chars_dict: Dict[str, str]) -> int:
    punctuation = """!?.,"'"<>«»:;{}[]()#$%^&*-+=/`~"""
    counter = 0
    for i in chars_dict.keys():
        if i in punctuation:
            counter += chars_dict[i]
    return counter


def count_non_ascii_chars(non_ascii_dict: Dict[str, str]) -> int:
    return sum((non_ascii_dict.values()))


def get_most_common_non_ascii_char(non_ascii_dict: Dict[str, str]) -> str:
    max_value_in_dict = max(non_ascii_dict.values())
    return get_key_by_value(non_ascii_dict, max_value_in_dict)

