class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class BST:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        print(f"{node.data}, ")
        if node.right:
            self.inorder(node.right)

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(f"{node.data}, ")

    def preorder(self, node):
        print(f"{node.data}, ")
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def insert(self, node, data):
        if self.root is None:
            self.root = Node(data)
        elif data > node.data:
            if node.right:
                self.insert(node.right, data)
            else:
                node.right = Node(data)
        elif data < node.data:
            if node.left:
                self.insert(node.left, data)
            else:
                node.left = Node(data)

    def search(self, node, data):
        if node is None:
            return
        elif data == node.data:
            return [True, node]
        elif data > node.data:
            if node.right:
                return self.search(node.right, data)
            else:
                return False
        elif data < node.data:
            if node.left:
                return self.search(node.left, data)
            else:
                return False

    @staticmethod
    def minvalue(node):
        i = node
        while i.left is not None:
            i = i.left
        return i

    def delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        elif data == node.data:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            elif node.right and node.left:
                temp = self.minvalue(node.right)
                node.data = temp.data
                node.right = self.delete(node.right, temp.data)
        return node


if __name__ == "__main__":
    bst = BST()
    lst = [4, 3, 26, 54, 34, 27, 54, 40, 30, 10, 36, 43]
    for i in lst:
        bst.insert(bst.root, i)
    print(bst.search(bst.root, 40))
    bst.inorder(bst.root)
    print()
    bst.root = bst.delete(bst.root, 40)
    print(bst.search(bst.root, 40))
    bst.inorder(bst.root)
    print()
    bst.preorder(bst.root)
    print()
    bst.postorder(bst.root)
