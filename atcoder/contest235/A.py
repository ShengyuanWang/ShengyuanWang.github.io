nums = list(input())
num1 = int(nums[0]+nums[1]+nums[2])
num2 = int(nums[1]+nums[2]+nums[0])
num3 = int(nums[2]+nums[0]+nums[1])
res = num1 + num2 + num3
print(res)