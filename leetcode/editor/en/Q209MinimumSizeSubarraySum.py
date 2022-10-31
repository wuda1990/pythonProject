# -*- coding: UTF-8 -*-
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, 
# numsr] of which the sum is greater than or equal to target. If there is no such 
# subarray, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem 
# constraint.
#  
# 
#  Example 2: 
# 
#  
# Input: target = 4, nums = [1,4,4]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  
# Follow up: If you have figured out the 
# O(n) solution, try coding another solution of which the time complexity is 
# O(n log(n)).
# 
#  Related Topics Array Binary Search Sliding Window Prefix Sum 👍 8145 👎 224


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = float("inf")
        Sum = 0
        start = 0
        for end in range(len(nums)):
            Sum += nums[end]
            while Sum >= target:
                length = min(length, end - start + 1)
                Sum -= nums[start]
                start = start + 1

        if length == float("inf"):
            return 0
        else:
            return length


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print("I'm a car!")
    solution = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    res = solution.minSubArrayLen(7, nums)
    print(res)

