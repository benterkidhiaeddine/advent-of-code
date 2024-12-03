from collections import Counter
f = open("input.txt", "r")
lines = f.read().split("\n")


# Number of occurences of numbers in second list from first list
map_1 = {}

result = 0

list_1 = []
list_2 = []

for line in lines:
    content = line.split("   ")
    list_1.append(int(content[0]))
    list_2.append(int(content[1]))

counter = Counter(list_2)
#print(counter)

for num in list_1:
    if num not in map_1:
        map_1[num] = 0


for num in list_2:
    if num in map_1:
        map_1[num] += 1

for num in list_1:
    result += num * map_1[num]

print(result)