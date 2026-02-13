
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

list1 = [1,2,4]
list2 = [1,3,4]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)


# wrong keep working
class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        list1_min = min(list1)
        list2_min = min(list2)

        start_of_head = 0

        # find smallest between two list to mark as head of linked list
        if list1_min > list2_min:
            start_of_head = list2_min
        elif list1_min < list2_min:
            start_of_head = list1_min
        else:
             start_of_head = list1_min

        # prepend to head
        head = ListNode(start_of_head)
        current = head
        
        # add to linked list
        for num in list1:
            current.next = ListNode(num)
            current = current.next
        
        return f'{head, 0}'



sol = Solution()
print(f'{sol.mergeTwoLists(list1, list2)}')