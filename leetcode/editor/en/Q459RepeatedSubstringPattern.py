# -*- coding: UTF-8 -*-
# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" 
# twice.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics String String Matching 👍 3983 👎 363


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        combine = (s + s)[1:-1]
        return combine.find(s) != -1

    def repeatedSubstringPatternKMP(self, s):
        length = len(s)
        if length == 0:
            return False
        next = self.getNext(s)
        return next[length - 1] != -1 and length % (length - next[length - 1] - 1) == 0

    # get the next arr of string
    def getNext(self, s):
        next = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            while s[i] != s[j + 1] and j > -1:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
        return next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPatternKMP("ababba"))
    # print(solution.repeatedSubstringPatternKMP('aba'))
    # print(solution.repeatedSubstringPatternKMP('abcabc'))
