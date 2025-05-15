class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create_bt(arr,i,n):
    if i>n:
        return None
    root=TreeNode(arr[i-1])
    root.left=create_bt(arr,2*i,n)
    root.right=create_bt(arr,2*i+1,n)
    return root
root=None
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


def levelorder(root):
    if root is None:
        return []
    result=[]
    queue=[root]
    while queue:
        node= queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 
    return result
def search_levelorder(root,ele):
    if root is None:
        return False
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        if node.data==ele:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
def search_preorder(root,ele):
    if root is None:
        return False
    if root.data==ele:
        return True
    return search_preorder(root.left,ele)or search_preorder(root.right,ele)


def search_inorder(root, ele):
    if root is None:
        return False
    if root.data == ele:
        return True
    return search_inorder(root.left, ele) or search_inorder(root.right, ele)

def search_postorder(root,ele):
    if root is None:
        return False
    if search_postorder(root.left,ele):
        return True
    if search_postorder(root.right,ele):
        return True
    if root.data==ele:
        return True
    return False




     


arr=[8,9,6,5,11]
btree=create_bt(arr,1,len(arr))
print("preorder Traversal")
preorder(btree)
print("\nInorder Traversal")
inorder(btree)

print("\nSearch 11 in inorder:", search_inorder(btree, 11))
print("\nSearch 11 in Preorder:", search_preorder(btree, 11))
print("\nSearch 11 in Postorder:", search_postorder(btree, 11))
print("\nSearch 11 in Level Order:", search_levelorder(btree, 11))




