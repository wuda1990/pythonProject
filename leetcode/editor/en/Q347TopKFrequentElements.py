# -*- coding: UTF-8 -*-
"""
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li> 
 <li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li> 
 <li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong> Your algorithm's time complexity must be better than <code>O(n log n)</code>, where n is the array's size.</p>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Divide and Conquer</li><li>Sorting</li><li>Heap (Priority Queue)</li><li>Bucket Sort</li><li>Counting</li><li>Quickselect</li></div></div><br><div><li>👍 16688</li><li>👎 615</li></div>
"""

import heapq
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i, v in enumerate(nums):
            map_[v] = map_.get(v, 0) + 1
        pri_queue = []
        for key, freq in map_.items():
            heapq.heappush(pri_queue, (freq, key))
            if len(pri_queue) > k:
                heapq.heappop(pri_queue)
        res = []
        for i in range(k):
            res.append(heapq.heappop(pri_queue)[1])
        return res[::-1]


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
out = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(out)
