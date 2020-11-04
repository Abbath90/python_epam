"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    list_ab = []
    list_cd = []
    counter = 0
    for i in a:
        for j in b:
            list_ab.append(i + j)
    for i in c:
        for j in d:
            list_cd.append(i + j)
    for i in list_ab:
        for j in list_cd:
            if (i + j) == 0:
                counter += 1
    return counter


"""a = [0, 2, 4]
b = [6, 8, 10]
c = [-6, -10, -12]
d = [-0, -16, -18]"""

a = [0]
b = [0]
c = [0]
d = [0]

print(check_sum_of_four(a, b, c, d))
