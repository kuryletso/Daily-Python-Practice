# Excercise: https://datalemur.com/questions/python-weakest-strong-link
#
#
# Solution:

def weakest_strong_link(strength):
    cols = list(zip(*strength))
    height, width = len(strength), len(strength[0])
    weakest_link = -1
    for i in strength:
        min_of_row = min(i)
        if min_of_row == max( cols[i.index(min_of_row)] ): weakest_link = min_of_row
    return weakest_link
	


if __name__ == "__main__":
    strength = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(weakest_strong_link(strength))
