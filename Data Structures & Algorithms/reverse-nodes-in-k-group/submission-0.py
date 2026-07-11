# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def skip(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        res = head

        for i in range(k - 1):
            if res == None:
                break
            res = res.next
        
        return res


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None


        tail = self.skip(head, k)

        if tail == None:
            return head



        next_head = tail.next
        tail.next = None

        curr = head
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    
        head.next = self.reverseKGroup(next_head, k)
        

        return prev