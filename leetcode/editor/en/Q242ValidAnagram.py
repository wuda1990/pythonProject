# -*- coding: UTF-8 -*-
# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 7680 👎 248


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count
    
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 定义一个字典，用来存储每个字符出现的次数
        char_count = {}
        # 遍历字符串s，统计每个字符出现的次数
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        # 遍历字符串t，判断每个字符是否出现过，以及出现的次数是否与s相同
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
        # 检查字典中是否所有字符的出现次数都为0
        for count in char_count.values():
            if count != 0:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.isAnagram2("hello", "lloeh"))
print(s.isAnagram2("hello1", "llo2eh2"))

