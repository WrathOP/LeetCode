# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tot = 0
        node = head
        while node: 
            node = node.next 
            tot += 1

        node = head
        first, last = None,None
        n=1
        while node:
            if first and last:
                break
            if n ==k:
                first = node
            if n== (tot-k+1):
                last = node
            node = node.next
            n+=1

        first.val,last.val= last.val,first.val 
        return head
    