# Excercise: https://www.hackinscience.org/exercises/caesar-cypher
#
#
# Solution:
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
length: int = len(lowercase)


def caesar_cypher_encrypt(s: str, key: int):
    result: str = ""
    for i in s:
        if i in lowercase:
            result += lowercase[(lowercase.find(i) + key) % length]
        elif i in uppercase:
            result += uppercase[(uppercase.find(i) + key) % length]
        else: result += i
    return result

def caesar_cypher_decrypt(s: str, key: int):
    result: str = ""
    for i in s:
        if i in lowercase:
            result += lowercase[(lowercase.find(i) - key) % length]
        elif i in uppercase:
            result += uppercase[(uppercase.find(i) - key) % length]
        else: result += i
    return result



if __name__ == "__main__":
    print(caesar_cypher_encrypt("Python is super disco !", 31))
    print(caesar_cypher_decrypt(caesar_cypher_encrypt("Python is super disco !", 31), 31))
