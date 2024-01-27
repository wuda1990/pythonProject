# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        pushes = 0
        i, j = 0, 0
        while i < length:
            j = i // 8 + 1
            pushes += j
            i += 1
        return pushes


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.minimumPushes("abcde"))
print(s.minimumPushes("xycdefghij"))
