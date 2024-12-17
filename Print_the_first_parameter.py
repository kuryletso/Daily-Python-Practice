# Excercise: https://www.hackinscience.org/exercises/print-the-first-parameter
#
#
# Solution:
import sys, re

def script_name() -> str:
    file_name: re.Match = re.search(r"[^\/]+\.py", sys.argv[0])
    if file_name:
        return file_name.group()

def first_param() -> None:
    try:
        f_param: str = sys.argv[1]
        print(f_param)
    except IndexError:
        print(f"usage: python3 {script_name()} PARAM")



if __name__ == "__main__":
    first_param()