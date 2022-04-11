# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        table = []
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy

        while curr:
            table.append(curr)
            curr = curr.next
        
        prev = table[len(table) - n - 1]
        delete = table[len(table) - n]
        prev.next = delete.next
        delete.next = None

        return dummy.next