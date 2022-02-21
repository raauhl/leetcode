class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        traversal = []
        stack = [root]
        
        while len(stack) != 0:
            
            node = stack.pop()
            traversal.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            
            if node.left is not None:
                stack.append(node.left)
        
        return traversal