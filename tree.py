# the tree data structure implementation using one class
class BTS:
    def __init__(self, root):
        self.root = root
        self.right_child = None
        self.left_child = None

    def is_empty_tree(self) -> bool:
        return self.root is None

    def insert_node(self, data):
        loop = 0
        if self.is_empty_tree():
            self.root = data
            print('The tree is empty')
            return
        if data < self.root:
            if self.left_child:
                loop += 1
                self.left_child.insert_node(data)
            else:
                self.left_child = BTS(data)
        elif data > self.root:
            if self.right_child:
                loop += 1
                self.right_child.insert_node(data)
            else:
                self.right_child = BTS(data)
                return

    def search_value(self, data):

        if self.is_empty_tree():
            self.root = data
            print('The tree is empty')
            return
        if data == self.root:
            print("A match has been found")
            return
        else:
            if self.left_child:
                self.left_child.search_value(data)
            if self.right_child:
                self.right_child.search_value(data)

    def pre_order_traversal(self):
        if self.is_empty_tree():
            print("Three is empty")
            return
        print(self.root, end=" ")
        if self.left_child:
            self.left_child.pre_order_traversal()
        if self.right_child:
            self.right_child.pre_order_traversal()

    def in_order_traversal(self):
        if self.is_empty_tree():
            print("Three is empty")
            return
        if self.left_child:
            self.left_child.pre_order_traversal()
        print(self.root, end=" ")
        if self.right_child:
            self.right_child.pre_order_traversal()

    def post_order_traversal(self):
        if self.is_empty_tree():
            print("Three is empty")
            return
        if self.left_child:
            self.left_child.pre_order_traversal()
        if self.right_child:
            self.right_child.pre_order_traversal()
        print(self.root, end=" ")

    def level_order_traversal(self):
        if self.is_empty_tree():
            print("Three is empty")
            return
        if self.left_child:
            self.left_child.pre_order_traversal()
        if self.right_child:
            self.right_child.pre_order_traversal()
        print(self.root, end=" ")
        print(self.left_child.root, end=" ")
        print(self.right_child.root, end=" ")

    def delete_node(self, node):
        if self.is_empty_tree():
            print("The tree is empty")
        if self.root < node:
            if self.left_child:
                self.left_child = self.left_child.delete_node(node)
            else:
                print('This node does not exist on the tree')
        elif self.root > node:
            if self.right_child:
                self.right_child = self.right_child.delete_node(node)
            else:
                print("This node does not exist on the tree")
        else:
            if self.left_child is None:
                temp_node = self.right_child
                self = None
                return temp_node
            if self.right_child is None:
                temp_node = self.left_child
                self = None
                return temp_node
            node = self.right_child
            while self.left_child:
                node = self.left_child
            self.root = node.roo
            self.right_child = self.right_child.delete_node(node.root)
        return self

    def get_min_node(self):
        while self.left_child:
            self = self.left_child
        print(f'The smallest node on the tree is: {self.root}')

    def get_max_node(self):
        while self.right_child:
            self = self.right_child
        print(f'The largest node on the tree is: {self.root}')

    def delete_root_node(self):
        pass


def tree_node_count(tree):
    if tree is None:
        return 0
    return 1 + tree_node_count(tree.left_child) + tree_node_count(tree.right_child)


if __name__ == "__main__":
    bts = BTS(10)
    bts.insert_node(11)
    bts.insert_node(4)
    bts.insert_node(2)
    bts.insert_node(1)
    bts.insert_node(0)
    bts.insert_node(23)
    bts.insert_node(34)
    bts.search_value(0)
    bts.post_order_traversal()
    bts.get_min_node()
    bts.get_max_node()
