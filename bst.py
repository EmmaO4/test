# https://www.geeksforgeeks.org/dsa/insertion-in-binary-search-tree

class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
    
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

# def insert(root, key):
#     temp = Node(key)

#     # If tree is empty
#     if root is None:
#         return temp

#     # Find the node who is going to 
#     # have the new node temp as its child
#     parent = None
#     curr = root
#     while curr is not None:
#         parent = curr
#         if curr.key > key:
#             curr = curr.left
#         elif curr.key < key:
#             curr = curr.right
#         else:
#             return root  # Key already exists

#     # If key is smaller, make it left 
#     # child, else right child
#     if parent.key > key:
#         parent.left = temp
#     else:
#         parent.right = temp

#     return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end =' ')
        inorder(root.right)

nums = [30, 20, 40, 70, 60, 80, 90]

for num in nums:
    insert(Node(num), num)

inorder(r)

# r = Node(50)
# r = insert(r, 30)
# r = insert(r, 20)
# r = insert(r, 40)
# r = insert(r, 70)
# r = insert(r, 60)
# r = insert(r, 80)