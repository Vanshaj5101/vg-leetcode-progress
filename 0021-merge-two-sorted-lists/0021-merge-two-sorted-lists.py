# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tmp = head
        s1 = list1
        s2 = list2
        while s1 and s2:
            f1 = s1.next
            f2 = s2.next
            if s1.val <= s2.val:
                tmp.next = s1
                s1 = f1
            else:
                tmp.next = s2
                s2 = f2
            tmp = tmp.next
        tmp.next = s2 if not s1 else s1
        return head.next