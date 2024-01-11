# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        """
        at every node the interesting information to have is the smallest and largest number from
        the left and right subtree. We can use these two values and compare with current node value
        to find out the largest absolute difference and keep track of it throughout the recursion.

        we return the new minimum and maximum back so that it can be used up.
        """
        
        def f(node):
                        
            if node.left is None and node.right is None:
                return (node.val, node.val)
            
            if node.left is not None and node.right is not None:
                
                miniLeft, maxxLeft = f(node.left)
                miniRight, maxxRight = f(node.right)
                
                mini = min(miniLeft, miniRight, node.val)
                maxx = max(maxxLeft, maxxRight, node.val)
                self.v = max(self.v, abs(node.val-mini), abs(node.val-maxx))
                
                return (mini, maxx)
                
            
            if node.left is not None:
                mini, maxx = f(node.left)
                self.v = max(self.v, abs(node.val-mini), abs(node.val-maxx))
                mini = min(mini, node.val)
                maxx = max(maxx, node.val)
                return (mini, maxx)
            
            if node.right is not None:
                mini, maxx = f(node.right)
                self.v = max(self.v, abs(node.val-mini), abs(node.val-maxx))
                mini = min(mini, node.val)
                maxx = max(maxx, node.val)
                return (mini, maxx)
                
        self.v = 0
        f(root)
        return self.v
    
