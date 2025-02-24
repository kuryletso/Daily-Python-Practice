
# Excercise: https://datalemur.com/questions/python-pascals-triangle
#
#
# Solution:

def generate(numRows):
    result: list[list] = [[1], [1, 1]]

    match numRows:
        case 0:
            return []
        case 1:
            return [[1]]
        case _:
            i = 2
            while i < numRows:
                print(i, result)
                new_row: list = [1] + [result[i-1][j] + result[i-1][j+1] for j in range(i-1)] + [1]
                result.append(new_row)
                i += 1
            return result
        


if __name__ =="__main__":
    n = 4
    print(generate(n))