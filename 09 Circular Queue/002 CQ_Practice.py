class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.item = [None] * size
        self.front = -1
        self.rear = -1

    # def is_empty(self):
    #     return self.front == -1
    
    # def is_full(self):
    #     return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, value):
        if ( (self.rear +1) %  self.front):
            print("Queue Overflow")

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.item[self.rear] = value
            print(f"Enqueued: {value}")
            
        else :
            self.rear = (self.rear + 1) % self.size
            self.item[self.rear] = value
            print(f"Enqueued: {value}")    
            
    def dequeue(self):
        if(self.front == -1):
                print("queue is empty")
        elif self.front == self.rear:
                print(self.item[self.front])
                self.front = self.rear = -1
        else:
            print(self.item[self.front])
            self.front = (self.front + 1) % self.size
            
soln = CircularQueue(5)
soln.enqueue(10)
soln.enqueue(20)
soln.enqueue(30)          

soln .dequeue()
soln .dequeue()