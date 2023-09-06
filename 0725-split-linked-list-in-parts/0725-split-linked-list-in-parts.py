# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lenLL = 0
        curr = head
        while curr:
            lenLL+=1
            curr = curr.next if curr.next else None
        lenSplit = lenLL//k
        extra = lenLL%k
        print(lenSplit,extra)
        res = []
        # prev = None
        curr = head
        for i in range(k):
            head = curr
            for j in range(lenSplit +(i< extra)-1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None , curr.next
            res.append(head)
        return res



