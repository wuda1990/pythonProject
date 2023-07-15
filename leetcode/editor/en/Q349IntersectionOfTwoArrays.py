# -*- coding: UTF-8 -*-
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must be unique and you may return the result in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
# 
#  Related Topics Array Hash Table Two Pointers Binary Search Sorting 👍 4023 👎
#  2043


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        var_dict = {}
        ans = []
        for i in nums1:
            var_dict[i] = 1
        for j in nums2:
            if j in var_dict.keys() and var_dict[j] == 1:
                ans.append(j)
                var_dict[j] = 0
        return ans

# leetcode submit region end(Prohibit modification and deletion)
