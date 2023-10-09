# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        buffer = deque()
        node = head
        while node:
            buffer.append(node.val)
            node = node.next
        n = len(buffer)

        buffer[k-1],buffer[n-k]= buffer[n-k],buffer[k-1]
        dummy = ListNode(0)
        curr = dummy
        while buffer:
            curr.next = ListNode(buffer.popleft())
            curr = curr.next

        return dummy.next
