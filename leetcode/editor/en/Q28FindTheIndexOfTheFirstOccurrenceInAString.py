# -*- coding: UTF-8 -*-
# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
# 
#  Related Topics Two Pointers String String Matching 👍 982 👎 78


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # bruce
    def strStrBruce(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    # use KMP to match subString
    def strStr(self, haystack, needle):
        nexts = self.getNext(needle)
        i, j = 0, -1
        while i < len(haystack):
            while j >= 0 and needle[j + 1] != haystack[i]:  # back track
                j = nexts[j]
            if needle[j + 1] == haystack[i]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
            i += 1
        return -1

    def getNext(self, s):
        next = [0] * len(s)
        j = -1
        next[0] = -1
        for i in range(1, len(s)):
            while s[i] != s[j + 1] and j >= 0:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
        return next


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.strStr("abcd", "ab"))
print(solution.strStr("abcd", "cd"))
