# Class for a Doubly LinkedList Node
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)  # dummy
        self.tail = Node(0, 0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def insertToHead(self, node: Node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            value = node.value
            self.removeNode(node)
            self.insertToHead(node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.insertToHead(node)
        else:
            # handles if capacity is reached
            if self.count >= self.capacity:
                tail_node = self.tail.prev
                self.removeNode(tail_node)
                del self.map[tail_node.key]
                self.count -= 1

            node = Node(key, value)
            self.map[key] = node
            self.insertToHead(node)
            self.count += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
