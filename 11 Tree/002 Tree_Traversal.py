#  TREE Traversal Example
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preorder(root):
    if root != None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")    
                
        
#        1
#      /   \
#     3     5
#    / \      \
#   2   4      8

root = Node(1)
root.left = Node(3)                   
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)
