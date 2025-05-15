class Circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=self.rear=-1
    def enqueue(self,data):
        if(self.rear+1)%self.size==self.front:
            print("Queue is full")
        elif self.front==-1:
            self.front=self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
    def display(self):
        if self.front==-1:
            print("queue is empty")
            return
        i=self.front
        while True:
            print(self.queue[i],end=" ")
            if i== self.rear:
                break
            i =(i+1)%self.size
        print()
cq=Circularqueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.display()



    
