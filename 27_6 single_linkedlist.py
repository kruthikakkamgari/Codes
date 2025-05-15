class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylinkedlist():
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
sll=Singlylinkedlist()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()


       
