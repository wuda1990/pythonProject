"""
Given the root of a binary tree, return the bottom-up level order traversal of 
its nodes' values. (i.e., from left to right, level by level from leaf to root). 


 
 Example 1: 
 
 
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
 

 Example 2: 

 
Input: root = [1]
Output: [[1]]
 

 Example 3: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 2000]. 
 -1000 <= Node.val <= 1000 
 

 Related Topics Tree Breadth-First Search Binary Tree 👍 4552 👎 316

"""
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode], res: List[List[int]], level: int):
        if root is None:
            return
        if len(res) == level:
            res.insert(0, [])
        res[-(level + 1)].append(root.val)
        self.levelOrder(root.left, res, level + 1)
        self.levelOrder(root.right, res, level + 1)

    def levelOrderBottom0(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.levelOrder(root, res, 0)
        return res

    # solution 2
    # use queue to traverse the tree level by level
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        while queue:
            res.insert(0, [])
            for _ in range(len(queue)):
                node = queue.pop(0)
                res[0].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# leetcode submit region end(Prohibit modification and deletion)
