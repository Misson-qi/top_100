# 力扣 热题100 · 第30题 两两交换链表中的节点
# 链接: https://leetcode.cn/problems/swap-nodes-in-pairs/
#
# ---------- 思路 ----------
# 题目在问什么：把链表中相邻两个节点两两交换，即第 1、2 个交换，第 3、4 个交换…。若节点数为奇数，最后一个不动。
#
# 做法：哑节点，pre 指向「当前要交换的那一对」的前一个节点。每次交换 pre.next（first）和 pre.next.next（second）：让 pre 指向 second，first 指向 second 后面的，second 指向 first；然后 pre 移到 first（即下一对的前驱）。直到没有成对的节点为止。
#
# ---------- 关键点 ----------
# · 要把 pre -> first -> second -> 后面 变成 pre -> second -> first -> 后面。顺序可以是：先 pre.next=second，再 first.next=second.next（把 first 接到 second 后面那段），再 second.next=first。这样不会断链。做完后 pre 移到 first，作为下一对的前驱。
# · 循环条件：pre.next 和 pre.next.next 都要存在才交换，否则没有「一对」可换，或 second 会变成 None。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            first, second = pre.next, pre.next.next
            pre.next = second
            first.next = second.next
            second.next = first
            pre = first
        return dummy.next
