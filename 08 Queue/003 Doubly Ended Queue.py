class DEQueue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)
        
    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
    
    def insertAtFront(self, value):
        self.items.insert(0, value)
        
    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop()    
 
dq = DEQueue()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtFront(40)
print(dq.items)

print("Deleted Element:", dq.deleteAtFront())
print(dq.items)  
      