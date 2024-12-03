

f = open("input.txt", "r")

lines = f.read().split("\n")



  
result = 0

for line in lines:
    nums = [int(i)  for i in line.split(" ")]
    good = False
    for j in  range(len(nums)):
        nums_1 = nums[:j] + nums[j+1:]
        print(nums_1)
        # if the list is equivelant to it's sorted version in ascending or descending then there is no change in direction
        asc_or_desc  = (nums_1 == sorted(nums_1) or nums_1 == sorted(nums_1, reverse=True))
        ok = True
        for i in range(len(nums_1) - 1):
            diff = abs(nums_1[i] - nums_1[i+1])
            if not 1 <= diff <=3:
                ok = False
        if asc_or_desc and ok:
            good = True 
    # we are assured that we always have a good list for already safe reports because when removing the last or the first items we will always have a safe report sub list
    if good:
        print("this never runs")
        result += 1 


print(result)

   
f.close() 