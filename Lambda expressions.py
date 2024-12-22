# Excercise: https://www.hackinscience.org/exercises/lambda-expressions
#
#
# Solution:

from collections.abc import Iterable, Callable
def filtered(items: Iterable,  filter: Callable) -> Iterable:
    types: dict = {"list" : list, "tuple": tuple, "set" : set}
    output: list = [item for item in items if filter(item)]
    try:
        return types[type(items).__name__](output)
    except KeyError:
        return output


if __name__ == "__main__":
    print(*filtered(range(101), lambda x: x % 3 == 0), sep=", ")
    print(*filtered(range(101), lambda x: x % 5 == 0), sep=", ")
    print(*filtered(range(101), lambda x: x % 15 == 0), sep=", ")