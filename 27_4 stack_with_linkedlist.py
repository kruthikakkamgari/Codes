class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.is_empty():
            print("Stack is underflow, cannot pop")
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        temp=self.top
        while temp:
            print(temp.data,end=" ")
            #def display(self):
               # print(temp.data,end=" ")
            temp=temp.next
        print("None")
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Popped:",stack.pop())
print("top element",stack.peek)
stack.display()




        