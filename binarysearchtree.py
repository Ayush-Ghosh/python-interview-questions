class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Insert method to create nodes
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.value:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.value:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.value) + ' is found')
            
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()
        print(self.value)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.PrintTree()
print(root.findval(7))
print(root.findval(14))