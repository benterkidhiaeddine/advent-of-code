# print(dimensions(lines))
import os

input_file_path = os.path.abspath("input.txt")
f = open(input_file_path, "r")


def dimensions(lines):
    return (len(lines), len(lines[0]))


lines = f.read().split("\n")


result = 0

n, m = dimensions(lines)

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if lines[i][j] != "A":
            continue
        top_left = lines[i - 1][j - 1]
        top_right = lines[i - 1][j + 1]
        bottom_right = lines[i + 1][j + 1]
        bottom_left = lines[i + 1][j - 1]
        corners = [top_left, top_right, bottom_right, bottom_left]
        str_corners = "".join(corners)
        if str_corners in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            result += 1


print(result)
f.close()
