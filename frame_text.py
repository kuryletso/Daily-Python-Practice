# Excercise: https://www.hackinscience.org/exercises/text-framing
#
#
# Solution:

from dataclasses import dataclass

@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"

fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")

def frame_text(text: str, frame: Frame) -> str:
    multiline = text.splitlines()
    longest: str = max(multiline, key = len)
    width = len(longest)

    top: str = frame.top_left + frame.top * width + frame.top_right
    bottom: str = frame.bottom_left + frame.bottom * width + frame.bottom_right
    middle: str = ""

    for i in multiline:
        middle += "\n" + frame.left + i + ( " " * (width - len(i)) ) + frame.right
    final_str: str = top + middle + "\n" + bottom
    return final_str


if __name__ == "__main__":
    sample_1 = "It is 16:04:37."
    sample_2 = """It is 16h19.
And it's raining."""

    print(frame_text(sample_2, fancy_frame))