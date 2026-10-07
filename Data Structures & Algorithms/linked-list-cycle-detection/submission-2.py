# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        poo = head
        doo = head.next
        while(doo and doo.next):
            if poo==doo:
                return True
            else:
                poo = poo.next
                doo = doo.next.next
        return False