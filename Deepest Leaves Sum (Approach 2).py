# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.ans = 0

        def findHeight(node):
            if not node:
                return 0
            x = findHeight(node.left)
            y = findHeight(node.right)
            return 1 + max(x, y)

        ht = findHeight(root)

        def findSum(node, height):
            if not node:
                return
            if height == ht:
                self.ans += node.val
            findSum(node.left, height + 1)
            findSum(node.right, height + 1)

        findSum(root, 1)
        return self.ans