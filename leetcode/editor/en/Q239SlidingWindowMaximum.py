# -*- coding: UTF-8 -*-
"""
<p>You are given an array of integers&nbsp;<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the max sliding window</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= k &lt;= nums.length</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Queue</li><li>Sliding Window</li><li>Heap (Priority Queue)</li><li>Monotonic Queue</li></div></div><br><div><li>👍 17649</li><li>👎 631</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myQueue = MyQueue()
        for i in range(k):
            myQueue.push(nums[i])
        res = [myQueue.front()]
        myQueue.pop(nums[0])
        len_ = len(nums)
        for i in range(1, len_ - k + 1):
            myQueue.push(nums[i + k - 1])
            res.append(myQueue.front())
            myQueue.pop(nums[i])
        return res


# The maximum is at the left
class MyQueue:
    def __init__(self):
        self.queue = deque()

    # push elements on the right side
    def push(self, x: int):
        while self.queue and x > self.queue[-1]:
            self.queue.pop()
        self.queue.append(x)

    # pop elements on the left side
    def pop(self, x: int):
        if self.queue and x == self.queue[0]:
            self.queue.popleft()

    def front(self):
        return self.queue[0]


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(solution.maxSlidingWindow([1], 1))
