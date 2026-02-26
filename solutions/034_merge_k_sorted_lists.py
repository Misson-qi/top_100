# 力扣 热题100 · 第34题 合并 K 个升序链表
# 链接: https://leetcode.cn/problems/merge-k-sorted-lists/
#
# ---------- 思路 ----------
# 题目在问什么：k 条升序链表，合并成一条升序链表。
#
# 做法：小根堆（最小堆）。先把每条链表的头节点入堆，堆里按节点的值排序（同时带上节点引用）。每次弹出值最小的节点，接到结果链的尾部，若该节点有 next 就把 next 入堆。这样每次取到的都是当前全局最小值，接完 N 个节点就得到完整结果。
#
# ---------- 关键点 ----------
# · 用一个小根堆，堆里存 (节点值, 编号, 节点引用)。每次弹出值最小的节点接到结果链后面，若该节点有 next 就把 next 入堆。这样每次取到的都是当前所有链里最小的那个，接完所有节点就得到合并后的有序链。堆里最多 k 个元素（每条链当前一个），所以总复杂度 O(N log k)。
# · 元组里加一个编号 i：因为 Python 的 heapq 在 val 相同时会比较下一项，节点可能不能比较，所以用 (val, i, node)，用 i 区分即可。

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        while heap:
            _, i, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
