class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Generally BST doesn't allow insertion of duplicate value
    def __insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.__insert(node.left, data)
        elif data > node.data:
            node.right = self.__insert(node.right, data)
        return node

    def __remove(self, node, data):
        if node is None:
            raise ValueError("Item not in Tree!")
        if data < node.data:
            node.left = self.__remove(node.left, data)
        elif data > node.data:
            node.right = self.__remove(node.right, data)
        else:
            if node.left is not None and node.right is not None:
                temp = self.min(node.right)
                node.data = temp.data
                node.right = self.__remove(node.right, temp.data)
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
        return node

    def __search(self, node, data):
        if node:
            if data < node.data:
                return self.__search(node.left, data)
            elif data > node.data:
                return self.__search(node.right, data)
            elif node.data == data:
                return True
        else:
            return False

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def remove(self, data):
        self.root = self.__remove(self.root, data)

    def search(self, data):
        return self.__search(self.root, data)

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)

    def preOrder(self, node):
        if node:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def levelOder(self):
        if self.root:
            que = [self.root]
            while que:
                temp = que.pop(0)
                print(temp.data, end=" ")
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            print()

    def min(self, node):
        if node is None:
            raise ValueError("Tree is empty!")
        while node.left:
            node = node.left
        return node


bst = BinarySearchTree()
bst.insert(70)
bst.insert(50)
bst.insert(30)
bst.insert(60)
bst.insert(20)
bst.insert(40)
bst.insert(90)
bst.insert(80)
bst.insert(100)
# bst.inOrder(bst.root)
# bst.remove(30)
bst.levelOder()
# print(bst.search(30))
bst.preOrder(bst.root)
