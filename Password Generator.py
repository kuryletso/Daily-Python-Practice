# Excercise: https://www.hackinscience.org/exercises/password-generator
#
#
# Solution:

from secrets import choice
from random import sample
from sys import exit
import string


def pwgen(length: int, with_digits: bool = True, with_uppercase: bool = True, with_spec_chars: bool = False) -> str:
    characters: str = string.ascii_lowercase + (with_digits * string.digits) + (with_uppercase * string.ascii_uppercase) + (with_spec_chars * string.punctuation)
    try:
        base_index: list = sample(range(length), 1 + with_digits + with_uppercase + with_spec_chars)
    except ValueError:
        print("Length is too small.")
    base_char: list[str] = [choice(string.ascii_lowercase)]
    if with_digits:
        base_char += choice(string.digits)
    if with_uppercase:
        base_char += choice(string.ascii_uppercase)
    if with_spec_chars:
        base_char += choice(string.punctuation)
    base: dict = dict(map(lambda x, y: (x, y), base_index, base_char))            
    
    password: str = ""
    try:
        for i in range(length):
            if i in base_index: password += base[i]
            else: password += choice(characters)
        return password
    except KeyError:
        print("Invalid parameter")


if __name__ == "__main__":
    print(pwgen(8))