# Excercise: https://www.hackinscience.org/exercises/side-by-side   |Solution:


import textwrap
from itertools import zip_longest


def sidebyside(left: str, right: str, width: int = 79) -> str:
    width //= 2
    full = zip_longest(textwrap.wrap(left, width=width-1), textwrap.wrap(right, width=width), fillvalue="")
    return "".join( f"{a:<{width-1}}|{b:<{width}}\n" for a, b in full )
        



############################################################################################################

text1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed non risus. 
Suspendisse lectus tortor, dignissim sit amet, 
adipiscing nec, utilisez sed sin dolor."""

text2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed non risus. 
Suspendisse lectus tortor, dignissim sit amet, 
adipiscing nec, utilisez sed sin dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed non risus. 
Suspendisse lectus tortor, dignissim sit amet, 
adipiscing nec, utilisez sed sin dolor."""

text3 = "Excercise: https://www.hackinscience.org/exercises/side-by-side"
text4 = "Solution:"

if __name__ == "__main__":
   print(sidebyside(text1, text2, 55))

