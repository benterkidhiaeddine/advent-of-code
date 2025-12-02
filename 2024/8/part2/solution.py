import os
import string
from collections import defaultdict
import itertools


def dimensions(M):
    return (len(M), len(M[0]))


def calculate_antinodes(start, end, n, m):
    antinodes_set = set()
    x_1, y_1 = start
    x_2, y_2 = end

    # Calculate deltas
    delta_x = x_2 - x_1
    delta_y = y_2 - y_1

    # Skip if points are the same
    if delta_x == 0 and delta_y == 0:
        return antinodes_set

    # Calculate antinodes in both directions
    # Forward direction
    c = x_1 + delta_x
    r = y_1 + delta_y
    while 0 <= c < m and 0 <= r < n:
        antinodes_set.add((c, r))
        c += delta_x
        r += delta_y

    # Backward direction
    c = x_1 - delta_x
    r = y_1 - delta_y
    while 0 <= c < m and 0 <= r < n:
        antinodes_set.add((c, r))
        c -= delta_x
        r -= delta_y

    return antinodes_set


def main():
    # Safely open and read file
    with open(os.path.abspath("input.txt"), "r") as f:
        lines = (
            f.read().splitlines()
        )  # Using splitlines() to handle different line endings

    # Remove any empty lines at the end
    lines = [line for line in lines if line]

    # Get dimensions
    n, m = dimensions(lines)
    print(n, m)

    # Find all antenna positions
    positions_per_char = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if lines[i][j] != ".":
                positions_per_char[lines[i][j]].append((j, i))

    # Calculate all antinodes
    all_antinodes = set()
    for key, value in positions_per_char.items():
        # Create all combinations of two for the same character
        two_point_combinations = list(itertools.combinations(value, 2))
        for combination in two_point_combinations:
            antinodes = calculate_antinodes(combination[0], combination[1], n, m)
            all_antinodes.update(antinodes)

    result = len(all_antinodes)
    print(result)


if __name__ == "__main__":
    main()
