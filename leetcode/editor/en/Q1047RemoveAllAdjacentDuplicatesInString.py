"""
<p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "abbaca"
<strong>Output:</strong> "ca"
<strong>Explanation:</strong> 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "azxxzy"
<strong>Output:</strong> "ay"
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>s</code> consists of lowercase English letters.</li> 
</ul>

<div><div>Related Topics</div><div><li>String</li><li>Stack</li></div></div><br><div><li>👍 6407</li><li>👎 241</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates1(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)

    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow, fast = 0, 0
        while fast < len(res):
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow - 1]:
                slow = slow - 1
            else:
                slow = slow + 1
            fast = fast + 1
        return "".join(res[0:slow])


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.removeDuplicates('abbadc'))
print(solution.removeDuplicates('c'))
