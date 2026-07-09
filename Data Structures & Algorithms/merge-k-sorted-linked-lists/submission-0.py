# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = 0
        queue = []

        for node in lists:
            if node:
                queue.append((node.val, counter, node))
                counter += 1

        heapq.heapify(queue)

        res = None
        tail = None

        while queue:
            _, _, node = heapq.heappop(queue)
            next = node.next

            if not res:
                res = node
                tail = node
            else:
                tail.next = node
                tail = tail.next

            if next:
                heapq.heappush(queue, (next.val, counter, next))
                counter += 1

        return res
