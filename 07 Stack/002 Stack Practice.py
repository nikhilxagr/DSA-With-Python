class stack:
    def __init__(self):
        self.s = []
        
    def length(self):
        return len(self.s)
    
    def is_empty(self):
        return self.length() == 0
    
    def push(self, value):
        self.s.insert(0, value)
        
    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        else:
            return self.s[0]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0)
        
stack1 = stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(stack1.peek())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

        