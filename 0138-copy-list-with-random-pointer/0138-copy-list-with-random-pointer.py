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
        if not head:
            return None
        tmp = head
        while tmp:
            newnode = Node(x=tmp.val, next=tmp.next)
            tmp.next = newnode
            tmp = newnode.next
        
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        
        head2 = tmp = head.next
        while tmp.next:
            tmp.next = tmp.next.next
            tmp = tmp.next
        
        return head2
