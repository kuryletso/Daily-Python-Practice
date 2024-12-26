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
    print_pascal_triangle(33)