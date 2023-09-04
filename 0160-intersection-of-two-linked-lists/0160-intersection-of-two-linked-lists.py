# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hm = set()
        dummy = headA
        while dummy:
            hm.add(dummy)
            dummy = dummy.next
        
        cur = headB
        while cur:
            if cur in hm:
                return cur
            cur = cur.next
        
        return None
