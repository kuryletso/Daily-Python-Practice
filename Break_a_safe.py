# Excercise: https://www.hackinscience.org/exercises/break-a-safe
#
#
# Solution:

import itertools


if __name__ == "__main__":
    digits: str = "158"
    for i in digits:
        combos = list(itertools.permutations(digits + i))
        for j in combos:
            print(*j)