# Excercise: https://www.hackinscience.org/exercises/adam-number
#
#
# Solution:

def check_adam_number(num):
    return int(str(num ** 2)[::-1]) == int(str(num)[::-1]) ** 2


if __name__ == "__main__":
    print(check_adam_number(15))