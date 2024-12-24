# Excercise: https://www.hackinscience.org/exercises/py-master-mind
#
#
# Solution:

import string
from random import choice

def gen_colors(nb_colors: int) -> str:
    # Generate colors
    return string.ascii_uppercase[:nb_colors]

def gen_code(code_size: int, colors: str) -> str:
    # Generate code
    return "".join(choice(colors) for _ in range(code_size))

def check_guess(guess: str, code_size: int, colors: str) -> bool:
    # Check if the guess has the same length as the code, and if each of its colors is part of the colors' list
    return len(guess) == code_size and all(char in colors for char in guess)

def score_guess(code, guess):
    # Indicate:
    # 1. The number of elements in the right position AND color
    # 2. The number of elements with the right color BUT in a wrong position
    a, b = 0, 0
    colors = "".join(set(code))
    for i in range(len(guess)):
        if guess[i] == code[i]:
            a+= 1
        else:
            if guess[i] in colors:
                b += 1
    return a, b

def play_cli(code_size, nb_colors):
    # Run a game
    colors: str = gen_colors(nb_colors)
    print(f"Possible colors are {colors}")
    code: str = gen_code(code_size, colors)
    print(f"Code is size {code_size}")

    score: tuple = 0, 0
    attempts: int = 0

    while score != (code_size, 0):
        guess: str = input("Enter your guess: ")
        guess.upper
        attempts += 1
        if check_guess(guess, code_size, colors):
            score = score_guess(code, guess)
            print(score)
        else: print("Wrong size or color !")
    print(f"Congrats, you won after {attempts} attempts !")



if __name__ == "__main__":
    play_cli(3, 3)