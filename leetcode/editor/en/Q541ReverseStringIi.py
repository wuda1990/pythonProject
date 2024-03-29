# -*- coding: UTF-8 -*-
# Given a string s and an integer k, reverse the first k characters for every 2
# k characters counting from the start of the string. 
# 
#  If there are fewer than k characters left, reverse all of them. If there are 
# less than 2k but greater than or equal to k characters, then reverse the first 
# k characters and leave the other as original. 
# 
#  
#  Example 1: 
#  Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  
#  Example 2: 
#  Input: s = "abcd", k = 2
# Output: "bacd"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics Two Pointers String 👍 1363 👎 2901


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        for i in range(0, length, 2 * k):
            right = i + k
            right = right if right < length else length
            s = s[:i] + s[i:right][::-1] + s[right:]
        return s

    def reverseStr2(self, s, k):
        length = len(s)
        s_list = list(s)
        for i in range(0, length, 2 * k):
            s_list[i:i + k] = s[i:i + k][::-1]
            # s_list[i:i + k] = reversed(s[i:i + k])
        return ''.join(s_list)


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.reverseStr2('abcdefg', 2))
print(solution.reverseStr2('abcdefgh', 3))
