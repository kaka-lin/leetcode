# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:        
#         dummy = ListNode(None)
#         dummy.next = head
#         root = dummy
#
#         while root.next and root.next.next:
#             prev, post = root.next, root.next.next
#             prev.next = post.next
#             post.next = prev
#             root.next = post
#             root = root.next.next
#            
#         return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pos = head.next
        head.next = self.swapPairs(head.next.next)
        pos.next = head
        return pos