# -*- coding: UTF-8 -*-
"""
<p>Given an array <code>nums</code> of <code>n</code> integers, return <em>an array of all the <strong>unique</strong> quadruplets</em> <code>[nums[a], nums[b], nums[c], nums[d]]</code> such that:</p>

<ul> 
 <li><code>0 &lt;= a, b, c, d&nbsp;&lt; n</code></li> 
 <li><code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code> are <strong>distinct</strong>.</li> 
 <li><code>nums[a] + nums[b] + nums[c] + nums[d] == target</code></li> 
</ul>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], target = 8
<strong>Output:</strong> [[2,2,2,2]]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 200</code></li> 
 <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li> 
 <li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Two Pointers</li><li>Sorting</li></div></div><br><div><li>👍 10664</li><li>👎 1270</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, _ in enumerate(nums):
            if nums[i] > target and nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > target and nums[i] > 0:
                    return res
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[i] + nums[j] + nums[right] < target:
                        left = left + 1
                    elif nums[left] + nums[i] + nums[j] + nums[right] > target:
                        right = right - 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right - 1]:
                            right = right - 1
                        left += 1
                        right -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 2, 2]
    res = solution.fourSum(nums, 8)
    print(res)
