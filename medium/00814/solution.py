# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)
        
    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            root.left = self.helper(root.left)
        if root.right:
            root.right = self.helper(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        else:
            return root
