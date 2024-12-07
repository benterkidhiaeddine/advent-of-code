import os

input_file_path = os.path.abspath("input.txt")
f = open(input_file_path, "r")

lines = f.read().split("\n")

OBSTACLE = "#"


unique_positions = set()


def dimensions(M):
    return (len(M), len(M[0]))


def copy_matrix(M):
    n, m = dimensions(M)
    new_M = [[None for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_M[i][j] = M[i][j]
    return new_M


def translate_matrix_to_map(M):
    n, m = dimensions(M)
    result = ""
    for i in range(n):
        for j in range(m):
            result += M[i][j]
        if i != n - 1:
            result += "\n"
    return result


n, m = dimensions(lines)


UP = "^"
DOWN = "V"
LEFT = "<"
RIGHT = ">"


def keep_moving_up(M, ix, iy):
    global unique_positions
    intial_ix, inital_iy = ix, iy
    while iy - 1 > -1 and M[iy - 1][ix] != OBSTACLE:
        iy -= 1
        unique_positions.add((ix, iy))

    new_M = copy_matrix(M)
    new_M[inital_iy][intial_ix] = "."
    new_M[iy][ix] = ">"
    return new_M, ix, iy


def keep_moving_down(M, ix, iy):
    global unique_positions
    n, m = dimensions(M)
    intial_ix, inital_iy = ix, iy
    while iy + 1 < n and M[iy + 1][ix] != OBSTACLE:
        iy += 1
        unique_positions.add((ix, iy))

    new_M = copy_matrix(M)
    new_M[inital_iy][intial_ix] = "."
    new_M[iy][ix] = "<"
    return new_M, ix, iy


def keep_moving_right(M, ix, iy):
    global unique_positions
    intial_ix, inital_iy = ix, iy
    while ix + 1 < m and M[iy][ix + 1] != OBSTACLE:
        ix += 1
        unique_positions.add((ix, iy))

    new_M = copy_matrix(M)
    new_M[inital_iy][intial_ix] = "."
    new_M[iy][ix] = "V"
    return new_M, ix, iy


def keep_moving_left(M, ix, iy):
    global unique_positions
    intial_ix, inital_iy = ix, iy
    while ix - 1 > -1 and M[iy][ix - 1] != OBSTACLE:
        ix -= 1
        unique_positions.add((ix, iy))

    new_M = copy_matrix(M)
    new_M[inital_iy][intial_ix] = "."
    new_M[iy][ix] = "^"
    return new_M, ix, iy


direction = "^"


ix, iy = 0, 0
for i in range(n):
    for j in range(m):
        if lines[i][j] == UP:
            ix, iy = j, i

M = copy_matrix(lines)
print(ix, iy)
print(translate_matrix_to_map(M))
while ix != 0 and ix != m - 1 and iy != 0 and iy != n - 1:
    if M[iy][ix] == UP:
        M, ix, iy = keep_moving_up(M, ix, iy)
        # print(translate_matrix_to_map(M))
    elif M[iy][ix] == RIGHT:
        M, ix, iy = keep_moving_right(M, ix, iy)
        # print(translate_matrix_to_map(M))
    elif M[iy][ix] == DOWN:
        M, ix, iy = keep_moving_down(M, ix, iy)
        # print(translate_matrix_to_map(M))
    elif M[iy][ix] == LEFT:
        M, ix, iy = keep_moving_left(M, ix, iy)
        # print(translate_matrix_to_map(M))
    print(ix, iy)

print(len(unique_positions))


# updated_matrix = keep_moving_up(lines, ix, iy)
# updated_matrix = translate_matrix_to_map(updated_matrix)
# print(updated_matrix)

result = 0


# print(result)
f.close()
