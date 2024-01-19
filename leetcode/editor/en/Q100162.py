# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = [0] * 101
        for i in nums:
            arr[i] += 1
        maximum = max(arr)
        res = 0
        for i in arr:
            if i == maximum:
                res += i
        return res


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(s.maxFrequencyElements([1, 2, 3, 4, 5]))
