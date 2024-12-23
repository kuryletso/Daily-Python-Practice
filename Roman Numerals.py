# Excercise: https://www.hackinscience.org/exercises/roman-numerals
#
#
# Solution:

def to_roman_numeral(num: int) -> str:
    # roman_units = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # roman_tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    # roman_hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    # roman_thousands = ["M", "MM", "MMM"]
    roman_numerals = [['M', 'MM', 'MMM'], ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
    roman = ""
    for i in range(1, 5):
        selector = num // (10 ** (4-i))
        if selector:
            roman += roman_numerals[i-1][selector-1]
        num %= (10 ** (4-i))
    return roman



if __name__ == "__main__":
    print(to_roman_numeral(1000))
