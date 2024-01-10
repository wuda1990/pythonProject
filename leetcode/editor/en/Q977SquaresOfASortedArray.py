# -*- coding: UTF-8 -*-
"""
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li> 
 <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li> 
 <li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li> 
</ul>

<p>&nbsp;</p> 
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an 
<code>O(n)</code> solution using a different approach?

<div><div>Related Topics</div><div><li>Array</li><li>Two Pointers</li><li>Sorting</li></div></div><br><div><li>👍 8112</li><li>👎 198</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.insert(0, nums[left] ** 2)
                left += 1
            else:
                res.insert(0, nums[right] ** 2)
                right -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

# main function to call above class
if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
