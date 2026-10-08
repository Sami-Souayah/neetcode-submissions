# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            left = same(root.left, subRoot.left)
            right = same(root.right, subRoot.right)

            return left and right

        def sub(root, subRoot):
            if not root:
                return False
            
            if same(root, subRoot):
                return True
            
            right = sub(root.right, subRoot)
            left = sub(root.left, subRoot)

            return left or right
        return sub(root, subRoot)
