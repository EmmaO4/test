class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

    @staticmethod
    def search(root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return Node.search(root.left, key)

        return Node.search(root.right, key)

    @staticmethod
    def insert(root, key):
        if root is None:
            return Node(key)
        if root.val == key:
            return root
        if key < root.val:
            root.left = Node.insert(root.left, key)
        else:
            root.right = Node.insert(root.right, key)
        return root
    
    
