# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        result_next=None

        ptr=head
        while True:
            old_next=ptr.next
            ptr.next=result_next
            result_next=ptr
            ptr=old_next
            if old_next==None:
                # this was the last node
                break
        return result_next

        





