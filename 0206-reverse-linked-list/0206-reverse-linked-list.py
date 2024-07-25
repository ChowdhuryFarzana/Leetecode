# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iteratively go through the list
        # time complexity O(N) and memory complexity O(1)
        
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            # reverse the current node's pointer 
            curr.next = prev
            prev = curr
            curr = nxt
        return prev 
        