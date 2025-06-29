# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify appending logic
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists while both have nodes
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append whatever remains from either l1 or l2
        tail.next = l1 if l1 else l2
        
        # The merged head is dummy.next
        return dummy.next
