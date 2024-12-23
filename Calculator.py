# Excercise: https://www.hackinscience.org/exercises/calculator1
#
#
# Solution:

import sys

def calculator() -> None:
    script_name: str = sys.argv[0]

    if len(sys.argv) < 4:
        print(f"usage: {script_name} a_number (an_operator +-*/%^) a_number")

    try: 
        code = " ".join(sys.argv[1:]).replace("^", "**")
        result = eval(code)
        print(result)
    except:
        print("input error")


if __name__ == "__main__":
    calculator()