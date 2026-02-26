# 力扣 热题100 · 第26题 环形链表 II
# 链接: https://leetcode.cn/problems/linked-list-cycle-ii/
#
# ---------- 思路 ----------
# 题目在问什么：若链表有环，找环的入口节点；无环返回 None。要求 O(1) 空间。
#
# 做法：先用快慢指针判断有环并让它们相遇。相遇后，把其中一个指针放回 head，两个指针都每次走 1 步，再次相遇的节点就是环入口（结论：从 head 到入口的距离 = 从相遇点到入口的距离）。
#
# ---------- 关键点 ----------
# · 先用快慢指针找到相遇点。结论：从 head 到环入口的距离 = 从相遇点到环入口的距离。所以相遇后，把一个指针放回 head，两个都每次走 1 步，再次相遇的节点就是环入口。（推导：设头到入口 a 步、环长 b，相遇时慢走了 a+c、快走了 a+c+k*b，且 2(a+c)=a+c+k*b，可得 a = k*b - c，即从 head 走 a 步和从相遇点走 a 步会到同一点，那就是入口。）
# · 无环时快指针会先到 None，循环退出返回 None。循环条件要写 fast and fast.next，避免访问空指针。

from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None
