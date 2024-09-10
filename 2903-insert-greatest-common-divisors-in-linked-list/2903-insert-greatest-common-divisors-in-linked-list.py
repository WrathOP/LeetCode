# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def EuclGCD(a,b):
            if a == 0:
                return a
            if b == 0:
                return b
            
            if a == b :
                return a
            
            if a > b:
                return EuclGCD(a-b,b)
            else:
                return EuclGCD(a,b-a)
        
        dummy = head

        while dummy and dummy.next:
            mid = EuclGCD(dummy.val,dummy.next.val)
            node= dummy.next
            dummy.next = ListNode(mid,node)
            dummy = dummy.next.next
            
        return head