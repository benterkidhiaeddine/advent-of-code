

f = open("input.txt", "r")

lines = f.read().split("\n")


def is_safe(nums: list[int]):

    direction = ""

    level_dampner = False
    l = len(nums)
    for i  in range(0, l - 1):
        if abs(nums[i] - nums[i+1]) > 3 or abs(nums[i] - nums[i+1]) < 1:
            return False
        
        if  direction == "":
            if nums[i+1] > nums[i]:
                direction = "asc"
            elif nums[i+1] < nums[i]:
                direction = "desc"

        elif direction  == "asc" and nums[i+1] < nums[i]:
            return False


        elif direction  == "desc" and nums[i+1] > nums[i]:
            return False
        
    return True


result = 0


for line in lines:
    nums = [int(i)  for i in line.split(" ")]
    if is_safe(nums):
        result += 1


print(result)

    