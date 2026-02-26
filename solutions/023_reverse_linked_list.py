# 力扣 热题100 · 第23题 反转链表
# 链接: https://leetcode.cn/problems/reverse-linked-list/
#
# ---------- 思路 ----------
# 题目在问什么：把一条链表反转，即每个节点的 next 指向前一个节点。
#
# 做法：用 prev 表示「已经反转好的那段」的头。每次拿当前节点 head，让 head.next 指向 prev，然后 prev 变成 head，head 移到原来的 head.next。直到 head 为 None，prev 就是新头。
#
# ---------- 关键点 ----------
# · 先把下一节点存下来：nxt = head.next，再改 head.next = prev。否则一改 head.next，就找不到原来的下一个节点了，没法继续往后遍历。
# · prev 一开始是 None：这样第一个节点反转后 next 指向 None，成为新链的尾。每步做完 prev=head，prev 就变成「已经反转好的那段」的新头。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
