# Binary tree is a tree data structure where node has most two children (left and right children)
# Root, parent, child are some of the terms

# Depth of Node: length of path from the root node to a node
# Height of Tree: length of path from the root node to the deepest descendant
# Complete Binary Tree: every level except possibly the last is completely filled and all nodes in the last level are far left
# Full Binary Tree: every node has 0 or 2 children

# Tree Traversal: process of visiting (checking or updating) each node in tree data structure once
# Unlike linked lists or 1-D arrays that are traversed linearly, trees can be traversed in depth-first or breadth-first order
# Depth-First Order: In-Order, Pre-Order, Post-Order

# Pre-Order (Depth-First):
#   1. Check if current node is empty/null
#   2. Display data of the current node
#   3. Traverse left subtree by recursively calling the method
#   4. Traverse right subtree by recursively calling the method

# In-Order (Depth-First):
#   1. Check if current node is empty/null
#   2. Traverse left subtree by recursively calling the method
#   3. Display data of the current node
#   4. Traverse right subtree by recursively calling the method

# Post-Order (Depth-First):
#   1. Check if current node is empty/null
#   2. Traverse left subtree by recursively calling the method
#   3. Traverse right subtree by recursively calling the method
#   4. Display data of the current node

# The output of the Depth-First methods will be different 
# (some outputs data before checking the subtrees resulting in the top node values displayed first before the bottom node values)

# Level-Order: create a queue and go through the nodes level by level
#   1. Enqueue root node
#   2. Dequeue from queue and add it to traversal
#   3. Enqueue the children of node that was dequeued
#   4. Dequeue the left node if existent, add it, and enqueue its children or nothing if no children
#   5. Dequeue the right node if existent, add it, and enqueue its children or nothing if no children
#   6. Keep going...

# Reverse Level-Order: create a queue and stack
#   1. Enqueue root node
#   2. Dequeue and push the root node value onto the stack
#   3. Enqueue the children of node that was dequeued (right first then left)
#   4. Dequeue and push the node values onto the stack
#   5. Keep going...
#   6. Pop from the stack until the stack is empty to get the traversed string

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    # Pre-Order (Depth-First) Traversal
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # In-Order (Depth-First) Traversal
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    # Post-Order (Depth-First) Traversal
    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    # Level-Order
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0: 
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
        
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    # Reverse Level-Order
    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)

    # Iterative for determining size
    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    # Recursive for determining size
    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.print_tree("reverse_levelorder"))