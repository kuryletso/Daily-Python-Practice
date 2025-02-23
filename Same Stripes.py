# Excercise: https://datalemur.com/questions/python-same-stripes
#
#
# Solution:


def is_same_stripes(matrix):
    height, width = len(matrix), len(matrix[0])
    for row in range(height-1):
        for col in range(width-1):
            if matrix[row][col] != matrix[row+1][col+1]: return False
    return True

      
    
    
    
if __name__ == "__main__":
    matrix = [
        ['a', 'b', 'c', 'd'],
        ['a', 'a', 'b', 'c'],
        ['e', 'a', 'a', 'b'],
        ['e', 'e', 'a', 'a']
    ]
    print(is_same_stripes(matrix))