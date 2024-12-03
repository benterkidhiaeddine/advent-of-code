import re
from functools import reduce

f = open("input.txt", "r")

text = f.read()

pattern = re.compile("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)")




result = re.findall(pattern=pattern, string=text)


calc = [int(x) * int(y) for x,y in result]
final_result = reduce(lambda a , b: a + b, calc)
# print(result)
print(calc)
print(final_result)
f.close()




    