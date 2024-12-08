# Excercise: https://www.hackinscience.org/exercises/count-the-lower-e-in-the-words-file
#
#
# Solution:

with open(r"words.txt", "r") as file:
    print( str(file.read()).count("e") )
