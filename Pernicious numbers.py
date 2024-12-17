# Excercise: https://www.hackinscience.org/exercises/pernicious-numbers
#
#
# Solution:

def isPrime(n: int) -> bool:
    if n % 2:
        for i in range(3, n // 2):
            if n % i == 0:
                return False
                break
        return True
    else: return False



def isPernicious(n: int) -> bool:
    return isPrime(bin(n).count("1"))



def main() -> None:
    for i in range(222281, 222381):
        if isPernicious(i): print(i)


if __name__ == "__main__":
    main()