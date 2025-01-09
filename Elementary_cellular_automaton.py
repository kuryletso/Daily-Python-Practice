# Excercise: https://www.hackinscience.org/exercises/elementary-cellular-automaton
#
#
# Solution:

from sys import argv

def elementary_automata(rule_num: int, width: int = 79, height: int = 40) -> str:

    fill_chars: tuple[str] = (".", "#")

    condition_preset: tuple[str] = ('111', '110', '101', '100', '011', '010', '001', '000')
    condition_preset = tuple(i.replace("0", fill_chars[0]).replace("1", fill_chars[1]) for i in condition_preset)
    rule: str = f"{bin(rule_num).replace("0b", ""):0>8}"
    rule = rule.replace("0", fill_chars[0]).replace("1", fill_chars[1])
    
    condition: dict[str, str] = {condition_preset[i]: rule[i] for i in range(len(condition_preset))}

    
    res_list: list[str] = []
    res_list.append(f"{"#":{fill_chars[0]}^{width}}")

    for row in range(1, height):
        res_list.append(
            condition[res_list[row-1][-1] + res_list[row-1][:2]]
            + "".join(condition[res_list[row-1][i-1:i+2]] for i in range(1, width-1))
            + condition[res_list[row-1][-2:] + res_list[row-1][0]]
        )
    
    return res_list



if __name__ == "__main__":
    try:
        rule_num: int = int(argv[1])
        if not 0 <= rule_num <= 255: print("Rule number must be between 0 and 255")
        else:
            print(*elementary_automata(rule_num), sep="\n")
    except IndexError:
        print(f"Valid syntax example: python3 {argv[0]} 90")
    except ValueError:
        print(f"Rule number must be an integer")