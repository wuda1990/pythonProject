# -*- coding: UTF-8 -*-
"""
<p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 × 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>2 &lt;= n &lt;= 58</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Math</li><li>Dynamic Programming</li></div></div><br><div><li>👍 3796</li><li>👎 369</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] = max(dp[i], max(j*dp[i-j], j*(i-j)))
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * dp[i - j], j * (i - j)))
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
