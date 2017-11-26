class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def inOrder(self):
        self.__inOrder(self.root)

    def __inOrder(self, root):
        if root == None:
            return
        self.__inOrder(root.left)
        print(root.val)
        self.__inOrder(root.right)

    def empty(self):
        return self.root == None

    def search(self, val):
        return self.__search(self.root, val)

    def __search(self, root, val):
        if root == None:
            print(val, "is not found.")
            return
        if(root.val == val):
            return root
        elif(root.val > val):
            return self.__search(root.left, val)
        else:
            return self.__search(root.right, val)

    def insert(self, val):
        node = Node(val)
        y = None
        x = self.root
        while(x):
            y = x
            if x.val > val:
                x = x.left
            elif x.val < val:
                x = x.right
            else:
                print('val has existed')
                return
        if not y:
            # when the tree is empty
            self.root = node
        else:
            node.parent = y
            if y.val > node.val:
                y.left = node
            else:
                y.right = node

    def delete(self, val):
        """
        delete 操作是BST-ADT中最复杂的操作
        :param val:
        :return:
        """
        node = None
        root = self.root
        while(root):
            if root.val == val:
                node = root
                break
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        if node:
            if (not node.left) or (not node.right):
                self.__delSingleChildNode(node)
            else:
                successor = self.successor(node)
                node.val = successor.val
                self.__delSingleChildNode(successor)

    def __delSingleChildNode(self, node):
        x = None
        if not node.left:
            x = node.right
        else:
            x = node.left
        x.parent = node.parent
        if node.parent.left == node:
            node.parent.left = x
        else:
            node.parent.right = x


    def max(self):
        root = self.root
        while(root.right):
            root = root.right
        return root

    def min(self):
        root = self.root
        while(root.left):
            root = root.left
        return root

    def successor(self, node):
        if not node:
            return
        res = None
        if node.right:
            node = node.right
            while(node):
                res = node
                node = node.left
        else:
            while(node.parent):
                if node == node.parent.left:
                    res = node.parent
                    break
                else:
                    node = node.parent
        return res

    def predecessor(self, node):
        if not node:
            return
        res = None
        if node.left:
            node = node.left
            while(node):
                res = node
                node = node.left
        else:
            while(node.parent):
                if node == node.parent.right:
                    res = node.parent
                    break
                else:
                    node = node.parent
        return res


root = BST()
root.insert(15)
root.insert(5)
root.insert(3)
root.insert(12)
root.insert(10)
root.insert(6)
root.insert(7)
root.insert(13)
root.insert(16)
root.insert(20)
root.insert(18)
root.insert(23)


root.delete(5)
root.inOrder()
print(root.successor(root.search(3)).val)