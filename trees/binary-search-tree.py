
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _insert(self, node, new_val):
        if (node.value > new_val):
            if node.left is not None:
                self._insert(node.left, new_val)
            else:
                node.left = Node(new_val)
        else:
            if node.right is not None:
                self._insert(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self._search(self.root, find_val)

    def _search(self, node, val):
        if node is not None:
            if node.value == val:
                return True
            elif node.value > val:
                return self._search(node.left, val)
            else:
                return self._search(node.right, val)
        else:
            return False

    def print_tree(self):
        return ""


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(3))
# Should be True
print(tree.search(5))
# Should be False
print(tree.search(40))
# Should be False
print(tree.search(6))
# Should print tree
print(tree.print_tree())
