# -*- coding: UTF-8 -*-
"""
<p>Given an array of <strong>distinct</strong> integers <code>nums</code> and a target integer <code>target</code>, return <em>the number of possible combinations that add up to</em>&nbsp;<code>target</code>.</p>

<p>The test cases are generated so that the answer can fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], target = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9], target = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 200</code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 1000</code></li> 
 <li>All the elements of <code>nums</code> are <strong>unique</strong>.</li> 
 <li><code>1 &lt;= target &lt;= 1000</code></li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong> What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?</p>

<div><div>Related Topics</div><div><li>Array</li><li>Dynamic Programming</li></div></div><br><div><li>👍 5896</li><li>👎 586</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1  # base case
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().combinationSum4([1, 2, 3], 4))
    print(Solution().combinationSum4([9], 3))
