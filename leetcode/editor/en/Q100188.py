# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dp = [[float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if i < n - 1:
                dp[i][i + 1] = 1
            if i > 0:
                dp[i][i - 1] = 1
        if x != y:
            dp[x - 1][y - 1] = 1
            dp[y - 1][x - 1] = 1
        # print(dp)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    dp[j][i] = dp[i][j]
        res = [0] * (n + 1)
        for i in range(n):
            for j in range(n):
                if dp[i][j] != float('inf'):
                    res[dp[i][j]] += 1
        return res[1:]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.countOfPairs(3, 1, 3))
# print(s.countOfPairs(5, 2, 4))
# print(s.countOfPairs(8, 2, 8))
print(s.countOfPairs(4, 1, 1))
