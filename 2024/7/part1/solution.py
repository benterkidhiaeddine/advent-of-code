import os
from itertools import product

path_abs = os.path.abspath("input.txt")
f = open(path_abs, "r")

lines = f.read().split("\n")


result = 0

possible_operations = ["+", "*"]

for line in lines:

    line_result = int(line.split(":")[0])
    nums_str = line.split(":")[1]
    nums_list = list(map(int, nums_str[1:].split(" ")))

    num_operations = len(nums_list) - 1

    combinations = list(product("+*", repeat=num_operations))

    for comb in combinations:
        temp_result = nums_list[0]
        for num, op in zip(nums_list[1:], comb):

            if op == "+":
                temp_result += num

            if op == "*":
                temp_result *= num

        if temp_result == line_result:
            result += line_result
            break


print(result)

f.close()
