"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Frame:
    
    def __init__(self, node):
        self.node = node
        self.next = 0

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        path = []
        if root is None:
            return path
        
        stack = [Frame(root)]
        while len(stack) > 0:
            
            frame = stack[-1]
            if frame.next <= len(frame.node.children) - 1:
                newFrame = Frame(frame.node.children[frame.next])
                stack.append(newFrame)
                frame.next += 1
            else:
                path.append(stack.pop().node.val)
        
        return path
                