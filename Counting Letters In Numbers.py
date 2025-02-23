# Excercise: https://datalemur.com/questions/python-counting-letters-in-numbers
#
#
# Solution:

def total_letters(N):

    def num_to_words(num):
        digits: dict = {
            0: '',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        }

        teens: dict = {
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen'
        }

        tens: dict = {
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety'
        }
        
        words: str = ''

        if num // 1000:
            words += digits[num // 1000] + 'thousand'
            num %= 1000
            # if num: words += ' '

        if num // 100:
            words += digits[num // 100] + 'hundred'
            num %= 100
            if num: words += 'and'

        if num // 10 > 1:
            words += tens[num // 10]
            num %= 10
            # if num: words += ' '
        elif num // 10 == 1:
            words += teens[num]
            num %= 1

        if num:
            words += digits[num]

        return words
    
    total_length = 0
    for num in range(1, N+1):
        total_length += len(num_to_words(num))
    return total_length



if __name__ == "__main__":
    print(total_letters(30))