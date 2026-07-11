# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr, l2_curr = l1, l2
        carry = False

        res = None
        curr = None

        while l1_curr or l2_curr:
            val = (l1_curr.val if l1_curr else 0) + (l2_curr.val if l2_curr else 0) + (1 if carry else 0)
            next_node = ListNode(val % 10)

            if val >= 10:
                carry = True
            else:
                carry = False
            
            if res == None:
                res = next_node
            else:
                curr.next = next_node
            
            if l1_curr:
                l1_curr = l1_curr.next
            
            if l2_curr:
                l2_curr = l2_curr.next
            curr = next_node
        
        if carry:
            curr.next = ListNode(1)
        
        return res