class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        
        stack1 = self.stack1
        stack2 = self.stack2
        
        if self.empty():
            print("Invalid Operation: pop on empty queue.")
            return sys.minsize
        
        if len(stack2) != 0:
            item = stack2.pop()
            return item
        
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        item = stack2.pop()
        return item

    def peek(self) -> int:
        
        stack1 = self.stack1
        stack2 = self.stack2
        
        if self.empty():
            print("Invalid Operation: peek on empty queue.")
            return sys.minsize
    
        if len(stack2) != 0:
            item = stack2[len(stack2)-1]
            return item
    
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        item = stack2[len(stack2)-1]
        return item
        

    def empty(self) -> bool:
        return (True if len(self.stack2) == 0 and len(self.stack1) == 0 else False)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()