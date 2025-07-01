# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        tmp = None
        
        while head2:
            succ = head2.next
            head2.next = tmp
            tmp = head2
            head2 = succ
        
        head2 = tmp
        # print(head, head2)

        # l1 = head
        # # l2 = head.next
        # r1 = head2
        # r2 = head2.next


        while head2:
            temp1=head.next
            temp2=head2.next
            head.next=head2
            head2.next=temp1
            head=temp1
            head2=temp2

        # while r1:
        #     l2 = l1.next
        #     r2 = r1.next
        #     l1.next = r1
        #     r1.next = l2
        #     l1 = l2
        #     r1 = r2
        #     l2 = l2.next
        #     r2 = r2.next
        # l1.next = r1
        # r1.next = l2

        # return head
        
        