from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeTraverser:
    def pre_traverse(self, root):
        if root is None:
            return []
        return [root.val] + self.pre_traverse(root.left) + self.pre_traverse(root.right)

    def intermediate_traverse(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.intermediate_traverse(root.left) + [root.val] + self.intermediate_traverse(root.right)

    def post_traverse(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.intermediate_traverse(root.left) + self.intermediate_traverse(root.right) + [root.val]

    def pre_traverse_iteratively(self, root: TreeNode):
        if root is None:
            return []
        st = [root]
        result = []
        while st:
            cur = st.pop()
            result.append(cur.val)
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
        return result

    def intermediate_traverse_iteratively(self, root: TreeNode):
        if root is None:
            return []
        result = []
        st = []
        cur = root
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                node = st.pop()
                result.append(node.val)
                cur = node.right
        return result

    def post_traverse_iteratively(self, root: TreeNode):
        if root is None:
            return []
        st = [root]
        result = []
        while st:
            cur = st.pop()
            result.append(cur.val)
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        return result[::-1]


traverser = TreeTraverser()
print(traverser.pre_traverse(TreeNode(3, TreeNode(2), TreeNode(4))))
print(traverser.intermediate_traverse(TreeNode(3, TreeNode(2), TreeNode(4))))
print(traverser.post_traverse(TreeNode(3, TreeNode(2), TreeNode(4))))
print(traverser.pre_traverse_iteratively(TreeNode(3, TreeNode(2), TreeNode(4))))
print(traverser.intermediate_traverse_iteratively(TreeNode(3, TreeNode(2), TreeNode(4))))
print(traverser.post_traverse_iteratively(TreeNode(3, TreeNode(2), TreeNode(4))))
