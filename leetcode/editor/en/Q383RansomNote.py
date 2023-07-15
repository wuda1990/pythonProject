# -*- coding: UTF-8 -*-
# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting 👍 3401 👎 389


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        arr = [0] * 26
        for x in magazine:
            arr[ord(x) - ord('a')] += 1
        for x in ransomNote:
            arr[ord(x) - ord('a')] -= 1
        for a in arr:
            if a < 0:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
s.canConstruct("aa", "aab")
