#TC - O(n)
#SC - O(h) 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = -1001
        self.dfs(root)
        return self.maximum
    
    def dfs(self,root):
        if root == None:
            return 0
        
        leftsum = max(self.dfs(root.left),0)
        rightsum = max(self.dfs(root.right),0)
        
        rootmax = leftsum+rightsum+root.val
        if self.maximum < rootmax:
            self.maximum = rootmax
        print(leftsum)
        print(rightsum)
       
            
        return root.val+max(leftsum,rightsum)