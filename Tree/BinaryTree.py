class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(temp):
    if temp:
        inOrder(temp.left)
        print(temp.data, end=" ")
        inOrder(temp.right)


def preOrder(temp):
    if temp:
        print(temp.data, end=" ")
        preOrder(temp.left)
        preOrder(temp.right)


def postOrder(temp):
    if temp:
        postOrder(temp.left)
        postOrder(temp.right)
        print(temp.data, end=" ")


# For O(1) time complexity use Queue using linked list implementation.
# Following implementation uses O(n) time complexity.
def levelOrder(temp):
    if temp:
        que = [temp]
        while que:
            node = que.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        print()


def search(temp, data):
    if temp:
        que = [temp]
        while que:
            node = que.pop(0)
            if node.data == data:
                return True
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        print()
    return False


# You must create root node first using Node() constructor to use this method.
def insert(temp, data):
    if temp:
        que = [temp]
        while que:
            node = que.pop(0)
            if node.left is not None:
                que.append(node.left)
            else:
                node.left = Node(data)
                return
            if node.right is not None:
                que.append(node.right)
            else:
                node.right = Node(data)
                return


def deleteDeepestNode(temp, deep_node):
    if temp:
        que = [temp]
        while que:
            node = que.pop(0)
            if node is deep_node:
                node = None
                return
            if node.right:
                if node.right is deep_node:
                    node.right = None
                    return
                else:
                    que.append(node.right)
            if node.left:
                if node.left is deep_node:
                    node.left = None
                    return
                else:
                    que.append(node.left)


def delete(temp, data):
    if temp:
        delete_node = None
        que = [temp]
        while que:
            node = que.pop(0)
            if node.data == data:
                delete_node = node
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        if delete_node:
            x = node.data
            deleteDeepestNode(temp, node)
            delete_node.data = x
        else:
            raise ValueError("Item not in Tree")


#                   4
#                 5    6
#              7    9


root = Node(4)
# root.left = Node(5)
# root.right = Node(6)
# root.left.left = Node(7)
# root.left.right = Node(9)
# inOrder(root)
# preOrder(root)
# postOrder(root)
# levelOrder(root)
# print(search(root, 9))
insert(root, 5)
insert(root, 6)
insert(root, 7)
insert(root, 9)
levelOrder(root)
delete(root, 5)
levelOrder(root)

