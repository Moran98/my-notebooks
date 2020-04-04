# @author Aaron Moran  
#
# Binary Trees - A binary tree has 1 parent and 2 children the next child is regarded as a sibling.
# Parent Node is the centre/head of the Tree. Regardless of its value. Larger Children Node values do not override the Parent.
# To be a Tree A Graph must satisfy two requirements -Acylic- and -Connected- 
#

class Node:

    def __init__(self, data):

        # left && right notes initialised to insert into tree
        self.left = None
        self.right = None
        self.data = data

    # inserting into the tree
    # data which is GREATER than PARENT will be inserted into the right
    # data which is LESS than PARENT will be insted into the left
    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            # if less than Parent Node go LEFT
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # if greater than Parent Node go RIGHT
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # else if insert(10) and parent(10) insert not entered or duplicated
        else:
            self.data = data

    # display the current tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


# User prompt
user_input = int(input("Enter the Parent Node value : "))
# Parent Node
root = Node(user_input)
# inserting into Nodes as child nodes, then to siblings
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(10)
root.insert(19)
root.insert(8)
# printing and displaying the tree
print("==========BINARY-TREE==========")
print("Parent is :", user_input)
print("-------------------------------")
root.PrintTree()