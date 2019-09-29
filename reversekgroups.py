# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        padd

    def reverseGroup(self, start: ListNode, k: int):

        try:
            end = get_nth_next(node, k + 1)
        except:
            return start
        for n in range(1, k, -2):
            a = get_nth_next(node, n)
            b = get_nth_next(node, n - 1)
            a.next = b
            b.next = end
            end = a

    def get_nth_next(node, n):
        old = node
        for n in range(n):
            if not node:
                raise ValueError("No more nodes")
            node = node.next
        return node