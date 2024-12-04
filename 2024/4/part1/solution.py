import os

input_file_path = os.path.abspath("input.txt")
f = open(input_file_path, "r")


WORD = "XMAS"


def dimensions(lines):
    return (len(lines), len(lines[0]))


# Search lines
def search_lines(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(n):
        for j in range(m):
            if (
                j + 3 < m
                and lines[i][j] == WORD[0]
                and lines[i][j + 1] == WORD[1]
                and lines[i][j + 2] == WORD[2]
                and lines[i][j + 3] == WORD[3]
            ):
                count += 1
    return count


# Search columns
def search_columns(lines):
    count = 0
    n, m = dimensions(lines)
    for j in range(m):
        for i in range(n):
            if (
                i + 3 < n
                and lines[i][j] == WORD[0]
                and lines[i + 1][j] == WORD[1]
                and lines[i + 2][j] == WORD[2]
                and lines[i + 3][j] == WORD[3]
            ):
                count += 1
    return count


# Search lines backwards
def search_lines_backwards(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if (
                j - 3 > -1
                and lines[i][j] == WORD[0]
                and lines[i][j - 1] == WORD[1]
                and lines[i][j - 2] == WORD[2]
                and lines[i][j - 3] == WORD[3]
            ):
                count += 1
    return count


# Search columns backwards
def search_columns_backwards(lines):
    count = 0
    n, m = dimensions(lines)
    for j in range(m):
        for i in range(n - 1, -1, -1):
            if (
                i - 3 > -1
                and lines[i][j] == WORD[0]
                and lines[i - 1][j] == WORD[1]
                and lines[i - 2][j] == WORD[2]
                and lines[i - 3][j] == WORD[3]
            ):
                count += 1
    return count


# Search Diagonals but only diagonals that are at least bigger than or equal to  4
def search_diagonals(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(m):
        for j in range(n):
            if (
                i + 3 < n
                and j + 3 < m
                and lines[i][j] == WORD[0]
                and lines[i + 1][j + 1] == WORD[1]
                and lines[i + 2][j + 2] == WORD[2]
                and lines[i + 3][j + 3] == WORD[3]
            ):
                count += 1
    return count


# Search Diagonals backwards but only diagonals that are at least bigger than or equal to  4
def search_diagonals_backwards(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(m):
        for j in range(n):
            if (
                i - 3 > -1
                and j - 3 > -1
                and lines[i][j] == WORD[0]
                and lines[i - 1][j - 1] == WORD[1]
                and lines[i - 2][j - 2] == WORD[2]
                and lines[i - 3][j - 3] == WORD[3]
            ):
                count += 1
    return count


# Search Diagonals backwards in columns but only diagonals that are at least bigger than or equal to  4
def search_diagonals_backwards_in_columns(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(m):
        for j in range(n):
            if (
                i + 3 < n
                and j - 3 > -1
                and lines[i][j] == WORD[0]
                and lines[i + 1][j - 1] == WORD[1]
                and lines[i + 2][j - 2] == WORD[2]
                and lines[i + 3][j - 3] == WORD[3]
            ):
                count += 1
    return count


# Search Diagonals backwards in columns but only diagonals that are at least bigger than or equal to  4
def search_diagonals_backwards_in_lines(lines):
    count = 0
    n, m = dimensions(lines)
    for i in range(m):
        for j in range(n):
            if (
                i - 3 > -1
                and j + 3 < m
                and lines[i][j] == WORD[0]
                and lines[i - 1][j + 1] == WORD[1]
                and lines[i - 2][j + 2] == WORD[2]
                and lines[i - 3][j + 3] == WORD[3]
            ):
                count += 1
    return count


lines = f.read().split("\n")


result = (
    search_lines(lines)
    + search_lines_backwards(lines)
    + search_columns(lines)
    + search_columns_backwards(lines)
    + search_diagonals(lines)
    + search_diagonals_backwards(lines)
    + search_diagonals_backwards_in_columns(lines)
    + search_diagonals_backwards_in_lines(lines)
)
print(result)
f.close()
