# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left-1):
            prev = prev.next
        
        stack = []
        current = prev.next

        for _ in range(right-left +1):
            stack.append(current)
            current = current.next
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        
        prev.next= current
        return dummy.next
        