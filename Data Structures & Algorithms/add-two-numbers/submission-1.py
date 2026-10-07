# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1=0
        len2=0
        ptr=l1
        while ptr is not None:
            len1+=1
            ptr=ptr.next
        ptr=l2
        while ptr is not None:
            len2+=1
            ptr=ptr.next
        tot=0
        ptr=l1
        for i in range(len1):
            tot += ptr.val * pow(10, i)
            ptr=ptr.next
            # len=3, i={0,1,2}
            # 10^2, 10^1, 10^0
            # len-i-1=3-0-1=2
            # 3-1-1=1
        ptr=l2
        for i in range(len2):
            tot += ptr.val * pow(10, i)
            ptr=ptr.next
        
        result=ListNode(tot%10)
        ptr=result
        tot=tot//10
        while tot>0:
            new_node=ListNode(tot%10)
            tot = tot // 10
            ptr.next=new_node
            ptr=new_node
        return result
            