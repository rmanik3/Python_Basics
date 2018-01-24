# Binary Search Tree in Python

class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild == Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False
        
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

bst = Tree()
print(bst.insert(5))
print(bst.insert(10))
print(bst.insert(2))
print(bst.find(5))
