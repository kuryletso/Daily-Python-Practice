# Excercise: https://www.hackinscience.org/exercises/my-add
#
#
# Solution:
import sys

def adder() -> None:
    script_name: str = sys.argv[0]
    if len(sys.argv) <= 1:
        print(f"usage: python3 {script_name} OP1 OP2")
    else:
        try:
            total: int = sum([int(i) for i in sys.argv[1:]])
            print(total)
        except ValueError:
            print(f"parameters must be of integer type")

if __name__ == "__main__":
    adder()