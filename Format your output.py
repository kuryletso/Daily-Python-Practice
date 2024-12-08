# Excercise: https://www.hackinscience.org/exercises/format-your-output
#
#
# Solution 1:

from collections.abc import Iterable

def list_pretty_print(items: Iterable) -> None:
    start, end = 0, 5
    last_row_cnt: int = len(items)%5
    while end <= len(items) - last_row_cnt:
        print(*items[start:end], sep=", ")
        start, end = end, end+5
    if last_row_cnt:
        print(*items[last_row_cnt * (-1):], sep=", ")


# Solution 2:

from itertools import batched

def list_pprint(items: Iterable) -> None:
    iterator = batched(items, 5)
    for _ in iterator:
        print(*_, sep=", ")





if __name__ == "__main__":
    mylist = [25] * 63
    list_pretty_print(mylist)
    print("\n")
    list_pprint(mylist)