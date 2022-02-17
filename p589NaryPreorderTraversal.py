"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Frame:
    def __init__(self, node):
        self.visited = False
        self.node = node
        self.next = 0

class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []
        
        traversal = []
        stack = [Frame(root)]
        
        while len(stack) > 0:
            frame = stack.pop()
            
            if not frame.visited:
                traversal.append(frame.node.val)
                frame.visited = True
                
            if frame.next <= len(frame.node.children)-1:
                nextNode = Frame(frame.node.children[frame.next])
                
                stack.append(frame)
                stack.append(nextNode)
                frame.next += 1
                      
        return traversal