import os
import string
from collections import defaultdict
import itertools

path_abs = os.path.abspath("input.txt")
f = open(path_abs, "r")

lines = f.read().split("\n")


def dimensions(M):
    return (len(M), len(M[0]))


# wholdes (x, y) pairs of unique antinodes coordinationsl
antinodes = set()


# go over the matrix looking for unique paris of simmilar antennas


n, m = dimensions(lines)
print(n, m)

positions_per_char = defaultdict(list)

for i in range(n):
    for j in range(m):
        if lines[i][j] != ".":
            positions_per_char[lines[i][j]].append((j, i))


for key, value in positions_per_char.items():
    # create all the combinations of two for the same character
    two_point_combinations = list(itertools.combinations(value, 2))
    for combination in two_point_combinations:
        x_1, x_2 = combination[0][0], combination[1][0]
        y_1, y_2 = combination[0][1], combination[1][1]
        first_antinode = (2 * x_1 - x_2, 2 * y_1 - y_2)
        second_antinode = (2 * x_2 - x_1, 2 * y_2 - y_1)

        if (
            first_antinode[0] >= 0
            and first_antinode[1] >= 0
            and first_antinode[0] < m
            and first_antinode[1] < n
        ):
            antinodes.add(first_antinode)
        if (
            second_antinode[0] >= 0
            and second_antinode[1] >= 0
            and second_antinode[0] < m
            and second_antinode[1] < n
        ):
            antinodes.add(second_antinode)


result = len(antinodes)
print(result)

f.close()
