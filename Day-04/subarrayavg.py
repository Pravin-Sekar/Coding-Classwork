"""643. Maximum Average Subarray I
Attempted
Easy
Topics
premium lock icon
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000"""


nums = [1, 12, -5, -6, 50, 3]
k = 4
window_sum = sum(nums[:k])
maxi = window_sum / k
    
for i in range(k, len(nums)):
    window_sum = window_sum - nums[i-k] + nums[i]
    avg = window_sum / k
    if avg > maxi:
        maxi = avg
            
print(maxi)



