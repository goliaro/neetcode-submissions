class Node:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.queue_head = None
        self.queue_tail = None
    
    def _update_pos(self, cur_node):
        if self.queue_tail != cur_node:
            if cur_node.prev is None:
                # it was the head
                assert self.queue_head == cur_node
                old_next = cur_node.next
                self.queue_head = old_next
                old_next.prev = None
            else:
                # middle -> just update pointers
                old_prev = cur_node.prev
                old_next = cur_node.next
                old_prev.next = old_next
                old_next.prev = old_prev
            cur_node.prev = self.queue_tail
            cur_node.next = None
            self.queue_tail.next = cur_node
            self.queue_tail = cur_node
        # else: do nothing

    def get(self, key: int) -> int:
        # print(f"get {key}")
        if key not in self.dic:
            return -1
        # move node to tail
        val, cur_node = self.dic[key]
        assert cur_node is not None

        self._update_pos(cur_node)

        return val
        
    def _evict(self):
        # print("\tevict")
        # print(self.dic)
        assert len(self.dic) == self.capacity
        key_to_evict = self.queue_head.key
        node_to_evict = self.queue_head
        old_next = node_to_evict.next
        # print("key_to_evict", key_to_evict)
        # print("node_to_evict:", node_to_evict)
        # print("head:", self.queue_head)
        # print("tail:", self.queue_tail)
        # print("old_next", old_next)
        
        if self.queue_head != self.queue_tail:
            assert self.capacity > 1
            self.queue_head = old_next
            old_next.prev = None
        else:
            assert self.capacity == 1
            assert old_next is None
            self.queue_head = None
            self.queue_tail = None

        del node_to_evict
        del self.dic[key_to_evict]


    def put(self, key: int, value: int) -> None:
        # print(f"put {key}->{value}")
        if key in self.dic:
            old_val, node = self.dic[key]
            self.dic[key] = (value, node)
            self._update_pos(node)
        else:
            if len(self.dic) == self.capacity:
                self._evict()
            new_node = Node(key)
            if self.queue_tail is not None:
                assert self.queue_head is not None
                new_node.prev = self.queue_tail
                self.queue_tail.next = new_node
            else:
                assert self.queue_head is None
                self.queue_head=new_node
            self.queue_tail=new_node
            self.dic[key] = (value, new_node)
    
        
# dict(key, (value, ptr in list))
# doubly linked list ordering by last use
# if get, use ptr to move node to head