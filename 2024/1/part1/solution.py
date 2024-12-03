f = open("input.txt", "r")
lines = f.read().split("\n")


sum = 0

list_1 = []
list_2 = []

for line in lines:
    content = line.split("   ")
    list_1.append(int(content[0]))
    list_2.append(int(content[1]))


list_1 = sorted(list_1)
list_2 = sorted(list_2)
 
 

for i in range(len(list_1)):
    sum += abs(list_2[i] - list_1[i])

print(sum)

f.close()