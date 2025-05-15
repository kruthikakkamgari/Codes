class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueue: {item}")

    def dequeue(self):
        if  self.is_empty():
            print("Queue is empty, cannot pop.")
            return None
        item =self.queue.pop(0)
        print("dequeue (item) from the queue")
        return None
    def peek(self):
        if  self.is_empty():
           print("Queue is empty, cannot peek.") 
           return None

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("Queue:", self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("Front elemnets:",queue.peek())
queue.dequeue()
queue.dequeue()
queue.display()
print("queue size",queue.size())
queue.dequeue()
queue.dequeue()
queue.display()
