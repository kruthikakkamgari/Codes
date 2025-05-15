class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
    def dequeue(self):
        if self.rear is None:
            print("Queue underflow cannot dequeue from a")
            return None
        dequeue_data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return dequeue_data
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data
    def is_empty(self):
        return self.front is None
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("None")
queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("dequeue:",queue.dequeue())
print("front element:",queue.peek())
queue.display()

    
    