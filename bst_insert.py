# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

def insert(self, val):
    new_node = Node(val)

    def searchTree(node):
        if val < node.info:
            if node.left is None:
                node.left = new_node
            else:
                searchTree(node.left)

        elif val > node.info:
            if node.right is None:
                node.right = new_node
            else:
                searchTree(node.right)

    if self.root:
        searchTree(self.root)
    else:
        self.root = new_node
        return
