# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = None
        while slow:
            tmp = slow.next
            slow.next = node
            node = slow
            slow = tmp
        first, second = head, node

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
