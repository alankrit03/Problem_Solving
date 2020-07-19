# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        pre = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack[-1]
            # print('here')
            if root.right == pre or (not root.right):
                # print('ere')
                ans.append(root.val)
                stack.pop()
                pre = root
                root = None
            else:
                root = root.right

        return ans