class Node():
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if node.data < data:
            node.Rchild = self._insert(node.Rchild, data)
        else:
            node.Lchild = self._insert(node.Lchild, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return None

        if node.data < data:
            return self._search(node.Rchild, data)
        elif node.data > data:
            return self._search(node.Lchild, data)
        else:
            return node.data

if __name__ == '__main__':
    ''''''