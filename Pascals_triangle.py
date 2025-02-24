
#                                 1
#                                1 1
#                               1 2 1
#                              1 3 3 1
#                             1 4 6 4 1
#                           1 5 10 10 5 1
#                         1 6 15 20 15 6 1
#                        1 7 21 35 35 21 7 1
#                      1 8 28 56 70 56 28 8 1
#                    1 9 36 84 126 126 84 36 9 1
#                1 10 45 120 210 252 210 120 45 10 1
#              1 11 55 165 330 462 462 330 165 55 11 1
#            1 12 66 220 495 792 924 792 495 220 66 12 1
#        1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1
#    1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1
# 1 15 105 455 1365 3003 5005 6435 6435 5005 3003 1365 455 105 15 1
#
# Excercise: https://www.hackinscience.org/exercises/pascals-triangle
#
#
# Solution:

def print_pascal_triangle(height):
    match height:
        case 1:
            print("1")
        case 2:
            print("""1
1 1""")
        case _:
            rows: list[list] = [[1], [1, 1]]
            r = 2
            while r < height:
                new_row: list = [1]
                new_row.extend(rows[r-1][n-1]+rows[r-1][n] for n in range(1, len(rows[r-1])))
                new_row.append(1)
                rows.append(new_row)
                r += 1

            rows = list(map(lambda x: " ".join(str(el) for el in x), rows))
            width: int = len(rows[-1])
            result: str = "\n".join(f"{row:^{width}}" for row in rows)
            print(result)


if __name__ == "__main__":
    print_pascal_triangle(16)