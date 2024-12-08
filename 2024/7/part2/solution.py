import os
from itertools import product
import time

path_abs = os.path.abspath("input.txt")
f = open(path_abs, "r")

lines = f.read().split("\n")


result = 0

possible_operations = ["+", "*", "||"]


t0 = time.time()
computations = {}
for line in lines:

    line_result = int(line.split(":")[0])
    nums_str = line.split(":")[1]
    nums_list = list(map(int, nums_str[1:].split(" ")))

    num_operations = len(nums_list) - 1

    combinations = list(product(possible_operations, repeat=num_operations))

    for comb in combinations:
        temp_result = nums_list[0]
        for num, op in zip(nums_list[1:], comb):

            if temp_result > line_result:
                break
            if op == "+":
                if (temp_result, num, op) in computations:
                    temp_result = computations[(temp_result, num, op)]
                else:
                    new_result = temp_result + num
                    computations[(temp_result, num, op)] = new_result
                    temp_result = new_result
            if op == "*":
                if (temp_result, num, op) in computations:
                    temp_result = computations[(temp_result, num, op)]
                else:
                    new_result = temp_result * num
                    computations[(temp_result, num, op)] = new_result
                    temp_result = new_result

            if op == "||":
                if (temp_result, num, op) in computations:
                    temp_result = computations[(temp_result, num, op)]
                else:
                    new_result = int(str(temp_result) + str(num))
                    computations[(temp_result, num, op)] = new_result
                    temp_result = new_result

        if temp_result == line_result:
            result += line_result
            break


print(result)
t1 = time.time()
elapsed_time = t1 - t0

print(elapsed_time)

f.close()
