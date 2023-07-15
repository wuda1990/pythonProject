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
    def minSubArrayLen1(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = float("inf")
        sum = 0
        start = 0
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                length = min(length, end - start + 1)
                sum -= nums[start]
                start = start + 1

        if length == float("inf"):
            return 0
        else:
            return length

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum = [0] * length
        sum[0] = nums[0]
        res = length + 1
        for i, _ in enumerate(nums[1:], 1):
            sum[i] = sum[i - 1] + nums[i]
        for i, _ in enumerate(nums):
            j = self.findRight(sum, i, length - 1, sum[i] + target - nums[i])
            if j != -1:
                res = min(res, j - i + 1)
        return 0 if res == length+1 else res

    def findRight(self, nums, left, right, target):
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[right] >= target:
            return right
        return -1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print("I'm a car!")
    solution = Solution()
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    res = solution.minSubArrayLen(11, nums)
    print(res)
    # sum = [2, 5, 6, 8, 12, 15]
    # print(solution.findRight(sum, 2, 5, 18))
