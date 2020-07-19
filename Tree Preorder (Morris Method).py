# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        while root:
            ans.append(root.val)
            if not root.left:
                root = root.right
            else:
                left = root.left
                while left.right:
                    left = left.right
                left.right = root.right
                root.right = None
                root = root.left
        return ans