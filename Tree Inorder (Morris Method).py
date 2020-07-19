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
        while node:
            if not node.left:
                ans.append(node.val)
                node = node.right
            else:
                left = node.left

                while left.right:
                    left = left.right
                left.right = node
                temp = node.left
                node.left = None
                node = temp
        return ans