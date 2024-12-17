# Excercise: https://www.hackinscience.org/exercises/print-parameters
#
#
# Solution:

import sys, re

def script_name() -> None:
    file_name: str = re.search(r"[^\/]+\.py", sys.argv[0])
    if file_name:
        print(file_name.group())

if __name__ == "__main__":
    script_name()