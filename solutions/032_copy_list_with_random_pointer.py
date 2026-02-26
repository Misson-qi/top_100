# 力扣 热题100 · 第32题 随机链表的复制
# 链接: https://leetcode.cn/problems/copy-list-with-random-pointer/
#
# ---------- 思路 ----------
# 题目在问什么：深拷贝一条链表，每个节点除了 next 还有 random 指针。要求 O(1) 额外空间（不含返回的链表）。
#
# 做法：第一步，在每个原节点后面插入一个拷贝节点（拷贝 val，next 指向原节点的 next）。第二步，设原节点 p，拷贝在 p.next；若 p.random 存在，则 p.next.random = p.random.next（因为 p.random 的拷贝就在 p.random 后面）。第三步，把原链和拷贝链拆开：遍历时把拷贝接到新链尾，并把原链的 next 恢复为原 next。
#
# ---------- 关键点 ----------
# · 第一步：在每个原节点后面插一个拷贝节点，原节点 p 的 next 指向拷贝，拷贝的 next 指向 p 原来的 next。这样「原节点-拷贝-原下一个」串在一起，拷贝和原节点一一对应，要找 p 的拷贝就是 p.next。
# · 第二步：若 p.random 指向某节点 B，那 p 的拷贝（p.next）的 random 应该指向 B 的拷贝（B.next），即 p.next.random = p.random.next。遍历一遍只改 random，不改 next。
# · 第三步：把拷贝节点从原链上拆下来接成新链，同时把原链的 next 恢复（p.next 改回 p.next.next）。拆的时候 p 每次往后跳时要注意：p 已经变成原下一个了，所以下一轮 p 用 copy.next。

from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        p = head
        while p:
            copy = Node(p.val, p.next, None)
            p.next = copy
            p = copy.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        dummy = Node(0)
        tail = dummy
        p = head
        while p:
            tail.next = p.next
            tail = tail.next
            p.next = p.next.next
            p = p.next
        return dummy.next
