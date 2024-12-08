# Excercise: https://www.hackinscience.org/exercises/give-the-frequency-of-letters-in-the-words-file
#
#
# Solution:

from string import ascii_lowercase

def let_freq(file) -> None:
    letters = {}
    with open(file, "r") as f:
        content = f.read()
        for letter in ascii_lowercase:
            letters[letter] = content.count(letter) / len(content)
    for key, value in letters.items():
        print(f"{key}: {value:.2f}")

file_name = r"words.txt"

if __name__ == "__main__":
    let_freq(file_name)