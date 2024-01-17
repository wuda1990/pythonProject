# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):

    def price(self, num, x):
        cnt = 0
        i = 1
        t = num
        while t > 0:
            if i % x == 0 and (t & 1) == 1:
                cnt += 1
            t = t >> 1
            i += 1
        return cnt

    def findMaximumNumber(self, k: int, x: int) -> int:
        total = 0
        num = 0
        while total <= k:
            num += 1
            total += self.price(num, x)
        if num == 0:
            return 0
        return num - 1


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.findMaximumNumber(9, 1))
print(s.findMaximumNumber(7, 2))
