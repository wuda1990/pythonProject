# -*- coding: UTF-8 -*-
"""
<p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>3 &lt;= nums.length &lt;= 3000</code></li> 
 <li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Two Pointers</li><li>Sorting</li></div></div><br><div><li>👍 29004</li><li>👎 2622</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        for i, _ in enumerate(nums):
            if nums[i] > 0:
                return r
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[i] + nums[right] < 0:
                    left = left + 1
                elif nums[left] + nums[i] + nums[right] > 0:
                    right = right - 1
                else:
                    r.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left += 1
                    right -= 1

        return r


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = solution.threeSum(nums)
    print(res)
