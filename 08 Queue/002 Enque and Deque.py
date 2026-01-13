class Queue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, value):
        self.items.append(value)
        
    def delete(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
 
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.items)

print("Deleted Element:", q.delete())
print(q.items)        