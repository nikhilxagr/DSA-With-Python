# Singly Linked List (MOST IMPORTANT)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self , head = None):
        self.head = head
        
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head !=None):
            t1 = self.head
            while(t1.next !=None):
                t1 = t1.next
            t1.next = temp
        else: 
            self.head = temp 
       
    def insertAtBegin(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
     
    def insertAtMiddle(self, value, pos): 
        temp = Node(value)
        t1 = self.head
        
        while (t1.next != None):
            if(t1.data == pos):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
     
    def deleteLL(self, value):
        t1 = self.head
        previous = t1
        if(t1.data == value):
            self.head = t1.next
            return
        while(t1.next != None):
            if(t1.data == value):
                previous.next = t1.next
                break
            else:
               previous = t1
               t1 = t1.next
        if(t1.data == value):
            previous.next = None       
             
    def printLL(self):
        t1 = self.head
        while(t1.next !=None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)     
                
            
obj = SinglyLinkedList()
obj.insertAtEnd(10)                 
obj.insertAtEnd(20)                 
obj.insertAtEnd(30) 
obj.insertAtBegin(5) 
obj.insertAtMiddle(15,10)
obj.deleteLL(20)
obj.printLL()          
            
                
                    
            
            
                