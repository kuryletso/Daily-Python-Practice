# Excercise: https://www.hackinscience.org/exercises/longest-collatz-sequence
#
#
# Solution:


def collatz_length(n: int) -> int:
    cnt: int = 0
    while n != 1:
        cnt += 1
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
    return cnt


if __name__ == "__main__":
    print(collatz_length(10))