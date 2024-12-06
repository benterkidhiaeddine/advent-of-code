import os

path_abs = os.path.abspath("input.txt")
f = open(path_abs, "r")

result = f.read().split("\n\n")

orederings = result[0].split("\n")

# dictionnary where the key must be before each number in list of value
before_after = {}

orderings_result = []
for item in orederings:
    x = int(item.split("|")[0])
    y = int(item.split("|")[1])
    orderings_result.append((x, y))

for item in orderings_result:
    if item[0] not in before_after:
        before_after[item[0]] = []
    before_after[item[0]].append(item[1])


list_result = []
lists = result[1].split("\n")
for item in lists:
    num_list = list(map(int, item.split(",")))
    list_result.append(num_list)


def is_after(num1, num2):
    return num2 in before_after[num1]


def correct_ordering(num_list):
    l = len(num_list)
    for i in range(l):
        for j in range(i):
            if num_list[i] in before_after and is_after(num_list[i], num_list[j]):
                return False
    return True


result = 0
for num_list in list_result:
    if correct_ordering(num_list):
        l = len(num_list)
        result += num_list[l // 2]


f.close()
