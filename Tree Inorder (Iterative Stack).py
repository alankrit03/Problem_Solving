# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        stack = []
        ans = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            curr = stack.pop()
            ans.append(curr.val)
            node = curr.right
        return ans