# finding the maximum subarray with the largest sum
nums = [-2, 1, -3, 4, 5, -1, 2, 1, -5, 4]

max_sum = nums[0]
current_sum = 0
subarrays = []  # To store all subarrays formed
current_subarray = []  # To track the current subarray
best_subarray = []  # To store the subarray with maximum sum

for num in nums:
    if current_sum < 0:
        current_sum = 0
        current_subarray = []  # Starting a new subarray
    
    current_sum += num
    current_subarray.append(num)
    subarrays.append(list(current_subarray))  # Storing a copy of the current subarray
    
    if current_sum > max_sum:
        max_sum = current_sum
        best_subarray = list(current_subarray)  # Storing a copy of the best subarray

print("Maximum sum:", max_sum)
print("\nAll subarrays formed:")
for i, sub in enumerate(subarrays, 1):
    print(f"Step {i}: {sub} (sum: {sum(sub)})")
    
print("\nSubarray with maximum sum:", best_subarray)