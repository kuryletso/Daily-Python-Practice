# Excercise: https://www.hackinscience.org/exercises/product-of-iterable
#
#
# Solution:

def mul(numbers: list):
    if numbers.count(0) > 0:
        return 0
    else:
        total: int = 1
        for n in numbers:
            total *= n
        return total


if __name__ == "__main__":
    mylist = [10, 10]
    mul(mylist)