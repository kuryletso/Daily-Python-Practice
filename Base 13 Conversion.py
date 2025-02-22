# Excercise: https://datalemur.com/questions/python-base-13-conversion
#
#
# Solution:

import string
chars = string.digits + string.ascii_uppercase[:3]

def convertToBase13(num):
    abs_num = abs(num)
    quotient = abs_num // 13
    remainder = abs_num % 13
    digits = chars[remainder]
    while quotient:
        quotient, remainder = quotient // 13, quotient % 13
        digits = chars[remainder] + digits
    if num < 0: return '-' + digits
    else: return digits


# Recursion solution
def convertToBase13_Recursion(num):
    sign = {0: '', 1: '-'}[num < 0]
    num = abs(num)
    if num // 13:
        return sign + convertToBase13_Recursion(num // 13) + chars[num % 13]
    else: return sign + chars[num]

if __name__ == "__main__":
    print(convertToBase13_Recursion(-1119817239821739821155123123123111845))