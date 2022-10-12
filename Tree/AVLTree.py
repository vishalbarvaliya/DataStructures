class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def remove(self, data):
        self.root = self.__remove(self.root, data)

    def __insert(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self.__insert(node.left, data)
        elif data > node.data:
            node.right = self.__insert(node.right, data)
        else:
            return node  # In case of avoid duplication

        # Increasing height of the node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        # Check for balance
        balance = self.__balanceFactor(node)
        if balance > 1:
            # Right rotate (Left Left condition)
            if data < node.left.data:
                return self.__rightRotate(node)
            # Left Right rotate
            elif data > node.left.data:
                node.left = self.__leftRotate(node.left)
                return self.__rightRotate(node)

        if balance < -1:
            # Left rotate (Right Right condition
            if data > node.right.data:
                return self.__leftRotate(node)
            # Right Left rotate
            elif data < node.right.data:
                node.right = self.__rightRotate(node.right)
                return self.__leftRotate(node)

        return node

    def __remove(self, node, data):
        if node is None:
            raise ValueError("Element not in the Tree!")
        elif data < node.data:
            node.left = self.__remove(node.left, data)
        elif data > node.data:
            node.right = self.__remove(node.right, data)
        else:
            if node.left is not None and node.right is not None:
                min_node = self.min(node.right)
                node.data = min_node.data
                node.right = self.__remove(node.right, min_node.data)
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
        if node is None:
            return node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        balance = self.__balanceFactor(node)

        if balance > 1:
            if self.__balanceFactor(node.left) >= 0:  # Left left (Right)
                return self.__rightRotate(node)
            else:     # Left Right
                node.left = self.__leftRotate(node.left)
                return self.__rightRotate(node)
        if balance < -1:
            if self.__balanceFactor(node.right) <= 0:
                return self.__rightRotate(node)
            else:
                node.right = self.__rightRotate(node.right)
                return self.__leftRotate(node)
        return node

    def min(self, node):
        if node is None:
            return node
        while node.left:
            node = node.left
        return node

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def __balanceFactor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def __rightRotate(self, node):
        temp = node.left
        node.left = temp.right  # node.left.right == temp.right
        temp.right = node
        # Height update
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        temp.height = max(self.height(temp.left), self.height(temp.right)) + 1
        return temp

    def __leftRotate(self, node):
        temp = node.right
        node.right = temp.left  # node.right.left == temp.left
        temp.left = node
        # Height update
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        temp.height = max(self.height(temp.left), self.height(node.right)) + 1
        return temp

    def levelOrder(self):
        if self.root is None:
            raise ValueError("Tree is empty!")
        que = [self.root]
        while que:
            temp = que.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                que.append(temp.left)
            if temp.right is not None:
                que.append(temp.right)


avl = AVLTree()
avl.insert(80)
avl.insert(50)
avl.insert(90)
avl.insert(30)
avl.insert(100)
avl.insert(20)
avl.remove(20)
avl.remove(90)
avl.remove(80)
avl.levelOrder()
