"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        mapping = {}
        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        for node in mapping:
            mapped = mapping[node]
            
            if node.next:
                mapped.next = mapping[node.next]
            
            if node.random:
                mapped.random = mapping[node.random]

        return mapping[head]