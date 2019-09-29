class Node:
    def __init__(self, key, val, nxt=None, lst=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.last = lst

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_head = None
        self.lru_tail = None
        self.lru_table = {}

    # most recently used goes at the head of the list.
    # when we get, move that node to the head of the list
    # ## write a method to do that since we'll have to do it in put as well
    #
    def get(self, key: int) -> int:
        node = self.lru_table.get(key, -1)
        if node == -1:
            return node
        self.lru_head, self.lru_tail = self.swap_head_with_node(self.lru_head, self.lru_tail, node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if not self.lru_head:
            self.lru_head = self.lru_tail = node
        # at capacity
        # get the tail of the list
        # drop it from the list
        # reset the tail of the list
        # delete that key from the table
        if len(self.lru_table) == self.capacity:
            lru = self.lru_tail
            self.lru_tail = lru.last
            if lru.last:
                lru.last.next = None
            lru.last = None
            del self.lru_table[lru.key]
        # make a node
        # put it at the head of the list
        # make head = node
        # table[node.val] = node
        node.next = self.lru_head
        self.lru_head.last = node
        self.lru_head = node
        self.lru_table[key] = nodea

    def swap_head_with_node(self, head, tail, node):
        if node == head:
            return head
        if node == tail:
            tail = node.last
        node.last.next = node.next
        if node.next:
            node.next.last = node.last
        node.next = head
        node.last = None
        head.last = node
        return node, tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)