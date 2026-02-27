
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# must conv from python list to linked list via user-defined method
list1 = [1,2,4]
list2 = [1,3,4]

class LLNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def build_ll(arr):
    head = LLNode()
    curr = head

    for num in arr:
        curr.next = LLNode(num)
        curr = curr.next
    return head.next

def print_ll(head):
    curr = head
    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next
    print("None")

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = LLNode()
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return head.next

list1 = build_ll(list1)
list2 = build_ll(list2)

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

print_ll(merged)