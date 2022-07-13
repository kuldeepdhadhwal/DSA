class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.inorder(root)
root.preorder(root)
root.postorder(root)
