# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        aa=[]
        def dfs(node,count):
            count+=1
            if not node:
                return count
            aa.append(count)
            
            dfs(node.left, count)
            dfs(node.right, count)
        dfs(root, 0)
        return max(aa)
        
