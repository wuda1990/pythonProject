# -*- coding: UTF-8 -*-
"""
<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>""</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
<strong>Explanation:</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "a", t = "aa"
<strong>Output:</strong> ""
<strong>Explanation:</strong> Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>m == s.length</code></li> 
 <li><code>n == t.length</code></li> 
 <li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li> 
 <li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>

<div><div>Related Topics</div><div><li>Hash Table</li><li>String</li><li>Sliding Window</li></div></div><br><div><li>👍 16340</li><li>👎 671</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # define two english letter array
        # one for t, one for s
        t_count = [0] * 128
        # count the number of each letter in t
        for i in t:
            t_count[ord(i) - ord('A')] += 1
        # define two pointers
        left = 0
        right = 0
        # define the minimum window
        min_window = s + ' '
        # define the number of letters in t
        t_num = len(t)
        # define the number of letters in s
        s_num = len(s)
        # define the number of letters in the window
        window_num = 0
        # define the number of letters in the window
        window_count = [0] * 128
        # define the number of letters in the window
        while right < s_num:
            # move right pointer
            window_count[ord(s[right]) - ord('A')] += 1
            if window_count[ord(s[right]) - ord('A')] <= t_count[ord(s[right]) - ord('A')]:
                window_num += 1
            # move left pointer
            while window_num == t_num:
                if right - left + 1 < len(min_window):
                    min_window = s[left:right + 1]
                window_count[ord(s[left]) - ord('A')] -= 1
                if window_count[ord(s[left]) - ord('A')] < t_count[ord(s[left]) - ord('A')]:
                    window_num -= 1
                left += 1
            right += 1
        if len(min_window) == s_num + 1:
            return ''
        else:
            return min_window


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow('cabwefgewcwaefgcf', 'cae'))  # cwae
