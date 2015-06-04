class BinaryTree:
    def __init__(self, root_data=None):
        self.root_data = root_data
        self.left_tree = None
        self.right_tree = None

    def append(self, data):
        if self.root_data is None:
            self.root_data = data
        elif data < self.root_data:
            if self.left_tree is None:
                self.left_tree = BinaryTree(root_data=data)
            else:
                self.left_tree.append(data)
        else: # data geq than root
            if self.right_tree is None:
                self.right_tree = BinaryTree(root_data=data)
            else:
                self.right_tree.append(data)


        
