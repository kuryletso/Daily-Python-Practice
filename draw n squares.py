def draw_n_squares(n: int) -> str:
    top_bottom = "+" + ("---+" * n)
    middle = "|" + ("   |" * n)
    table = top_bottom + ("\n" + middle + "\n" + top_bottom) * n
    return table


if __name__ == "__main__":
    print(draw_n_squares(15))