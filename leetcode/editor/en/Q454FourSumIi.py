# -*- coding: UTF-8 -*-
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
# return the number of tuples (i, j, k, l) such that: 
# 
#  
#  0 <= i, j, k, l < n 
#  nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1)
#  + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1)
#  + 0 = 0
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums1.length 
#  n == nums2.length 
#  n == nums3.length 
#  n == nums4.length 
#  1 <= n <= 200 
#  -2²⁸ <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2²⁸ 
#  
# 
#  Related Topics Array Hash Table 👍 4260 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict
        n, hm, count = len(nums1), defaultdict(lambda: 0), 0
        for i in nums1:
            for j in nums2:
                hm[i + j] += 1

        for k in nums3:
            for l in nums4:
                count += hm[0 - (k + l)]
        return count
# leetcode submit region end(Prohibit modification and deletion)
