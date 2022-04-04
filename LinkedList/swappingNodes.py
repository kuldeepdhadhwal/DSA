# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#   https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l = r = head
        for _ in range(k-1):
            l = l.next
            
        tail = l
        while tail.next:
            r, tail = r.next, tail.next
        l.val, r.val = r.val, l.val
        return head
