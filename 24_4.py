class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            #print("Stack is empty, cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
stack.pop()
stack.display()
