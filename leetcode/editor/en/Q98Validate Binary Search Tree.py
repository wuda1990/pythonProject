"""
<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul> 
 <li>The left <span data-keyword="subtree">subtree</span> of a node contains only nodes with keys <strong>less than</strong> the node's key.</li> 
 <li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node's key.</li> 
 <li>Both the left and right subtrees must also be binary search trees.</li> 
</ul>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" /> 
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" /> 
<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li> 
 <li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Tree</li><li>Depth-First Search</li><li>Binary Search Tree</li><li>Binary Tree</li></div></div><br><div><li>👍 15589</li><li>👎 1270</li></div>
"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


        
# leetcode submit region end(Prohibit modification and deletion)
