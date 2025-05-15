class TreeNode:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def createbst(root,val):
    if root is None:
        return TreeNode(val)
    else:
        if root.data==val:
            return root
        elif root.data<val:
            root.right=createbst(root.right,val)
        else:
            root.left=createbst(root.left,val)
        return root
def find_min(root):
    while root.left is not None:
        root=root.left
    return root
def delete_node(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete_node(root.left,key)
    elif key > root.data:
        root.right=delete_node(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp=find_min(root.right)
        root.data=temp.data
        root.right=delete_node(root.right,temp.data)
    return root
def update_node(root,old_val,new_val):
    root=delete_node(root,old_val)
    root=createbst(root,new_val)
    return root
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
arr=[8,3,10,1,6,14,4,7]
root=TreeNode(arr[0])
for i in range(1,len(arr)):
    root=createbst(root,arr[i])
print("preorder Traversal: ",end="")
preorder(root)
print()





        