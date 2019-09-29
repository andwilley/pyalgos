# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop

class SortableNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __repr__(self):
        return f"<SNode val: {self.node.val}>"

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        so...
        this is basically take the min of the head of every list,
        advnace that list,
        add it to the new list

        however: this could get ugly, because min will be linear on the heads of the list for each item in the resulting
        list, which duplicates a lot of comparisons

        maybe keep the current min with an index and check it with the new one
        if we use the min, replace it with the last one

        this might work with a stack of mins, push when greater than or equal to, pop to get the min
        this will be as big as the number of lists until lists start running out

        when the stack runs out though, we have to do the same linear search of the heads. at worst, this is still
        linear on the heads of the list times the length of the longest

        keep heads in a min-heap, logn to push the next min * longest list
        """

        heap = []

        for node in lists:
            if node:
                heappush(heap, SortableNode(node))

        if not heap:
            return None

        head = heappop(heap).node
        if head.next:
            heappush(heap, SortableNode(head.next))
        curr = head

        while heap:
            curr.next = heappop(heap).node
            nxt = curr.next.next

            curr = curr.next

            if nxt:
                heappush(heap, SortableNode(nxt))

        return head