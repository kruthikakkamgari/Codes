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
         
            
