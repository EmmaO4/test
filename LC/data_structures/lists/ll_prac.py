import timeit
"""
make Linked List
make python list (array)
compare big O between two using import time
bonus: double linked list
"""

class LLNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_ll(nums):
    head = LLNode()
    curr = head

    for num in nums:
        curr.next = LLNode(num)
        curr = curr.next
    
    return head.next

def print_ll(node):
    while node:
        print(node.val, end=' -> ')
        node = node.next
    print('none')

def front_insert(head, val):
    newNode = LLNode(val)
    newNode.next = head
    return newNode


arr = [7, 2, 4, 1, 8, 3, 9]

built = build_ll(arr)

print_ll(built)
head = front_insert(built, 1)
# ---------------------
# for _ in range(1_000_000):
#     head = front_insert(built, 1)

# end = time.perf_counter()

benchmarking = timeit.timeit("front_insert(built, 1)", globals=globals(), number=1_000_000)

# ---------------------

print_ll(head)
print(f'runtime: {benchmarking}')