# finding the maximum subarray with the largest sum

nums = [-2,1,-3,4,5,-1,2,1,-5,4]

maxSub = nums[0]
curr_sum = 0

for i in nums:
    if curr_sum < 0:
        curr_sum = 0 
    curr_sum += 1
    maxSub = max(maxSub, curr_sum)
print(maxSub)