import re
from functools import reduce

f = open("input.txt", "r")

text = f.read()

pattern = re.compile("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)|(do\(\))|(don't\(\))")




result = re.findall(pattern=pattern, string=text)

final_result = 0
#print(result)
enabled = True
for item in result:
    print(item)
    if item[0] != "" and enabled:
        print(item)
        final_result += int(item[0]) * int(item[1])
    elif item[2] != "":
        enabled = True
    elif item[3] != "":
        enabled = False


print(final_result)
        
#calc = [int(x) * int(y) for x,y in result]
#final_result = reduce(lambda a , b: a + b, calc)
# print(result)
#print(calc)
#print(final_result)
f.close()




    