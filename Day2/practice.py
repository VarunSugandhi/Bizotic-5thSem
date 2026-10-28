'''
a = [2,3,7,4,5]
target = 12
output = index of the two numbers that add up to the target
'''

nums = [1,2,3,7,5]
target = 12

s = 0
l = len(nums) - 1
sum = 0
while(s < l):
    sum = nums[s] + nums[l]
    if sum == target:
        print("The two nor that add up till target:", nums[s], "and", nums[l], "and their indices are:", s, "and", l)
        break
    elif sum < target:
        s += 1
    else:
        l -= 1
