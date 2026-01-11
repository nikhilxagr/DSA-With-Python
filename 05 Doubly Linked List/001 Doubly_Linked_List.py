class Node :
    def __init__(self, data = None) :
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList :
    def __init__(self) :
        self.head = None
        
    def InsertAtEnd(self, data) :
        temp = Node(data)
        if (self.head is None) :
            self.head = temp
            return
        
        t = self.head
        while (t.next is not None) :
            t = t.next
            
        t.next = temp
        temp.prev = t
        
    def InsertAtBeginning(self, data) :
        temp = Node(data)
        if (self.head is None) :
            self.head = temp
            return
        
        temp.next = self.head
        self.head.prev = temp
        self.head = temp    
        
    def InsertAtPosition(self, data, pos) : 
        t = self.head
        temp = Node(data)
        while (t.next != None):
            if(t.data == pos):
                break
            else:
                t = t.next
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t     
        
    def Display(self) :
        t = self.head
        while (t is not None) :
            print(t.data, end = " ")
            t = t.next
        print()  
        
    def deletionDLL(self, data):  
        if(self.head is None):
            print("DLL is empty")
            return
        
        t = self.head
        if(t.data == data):
            self.head = t.next
            self.head.prev = None
            t = None
            return
        
        while( t.next != None):
            if(t.data == data):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else :
                t = t.next
            if(t.next.data == data):
                t.prev.next = None
        
obj = DoublyLinkedList()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtBeginning(5)
obj.InsertAtPosition(15, 10)
obj.deletionDLL(5)
obj.deletionDLL(20)

obj.Display()


