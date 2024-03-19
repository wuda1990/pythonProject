class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PreTraverser:
    def traverse(self, root):
        if root is None:
            return []
        return [root.val] + self.traverse(root.left) + self.traverse(root.right)


traverser = PreTraverser()
print(traverser.traverse(TreeNode(3, TreeNode(2), TreeNode(4))))
