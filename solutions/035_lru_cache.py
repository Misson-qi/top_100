# 力扣 热题100 · 第35题 LRU 缓存
# 链接: https://leetcode.cn/problems/lru-cache/
#
# ---------- 思路 ----------
# 题目在问什么：实现 LRU（最近最少使用）缓存。get(key) 取值并在用过后算「最近使用」；put(key,value) 放入，若容量满则淘汰「最久没用的」再放入。get/put 都要 O(1)。
#
# 做法：哈希表存 key→节点，方便 O(1) 查；双向链表按「使用时间」排序，最近用的在头、最久未用的在尾。get 时若存在则把该节点移到头（删掉再插到头）；put 时若 key 已存在则更新值并移到头，否则在头插入新节点，若 size>capacity 则删掉尾节点并在哈希表里删掉对应 key。
#
# ---------- 关键点 ----------
# · 用「哈希表 + 双向链表」：哈希表按 key 找到节点，O(1)；链表按「使用时间」排，头是最近用的、尾是最久未用的，删尾、插头、把某节点移到头都是 O(1)。单用哈希表不知道谁最久未用，单用链表无法按 key 快速找节点。
# · 必须用双向链表：要把中间某个节点移到头或从尾部删掉，都要改它的前一个的 next，单向链表找前驱要遍历，双向链表有 prev 就行。
# · 哑头哑尾：head 和 tail 不存数据，这样头插总有 head.next 可挂，删尾时 tail.prev 就是最久未用的。put 时若 key 已存在，除了改 value 还要把该节点移到头（算一次访问）；满了就删 tail.prev 并在哈希表里删掉对应 key。

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: DLinkedNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: DLinkedNode) -> None:
        self._remove(node)
        self._add(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return
        node = DLinkedNode(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            tail = self.tail.prev
            self._remove(tail)
            del self.cache[tail.key]
