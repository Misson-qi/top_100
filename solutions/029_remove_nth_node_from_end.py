# 力扣 热题100 · 第29题 删除链表的倒数第 N 个结点
# 链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
#
# ---------- 思路 ----------
# 题目在问什么：删掉链表倒数第 n 个节点，返回头节点。保证 n 有效。
#
# 做法：哑节点接在 head 前（方便删头节点）。快指针先走 n+1 步，然后快慢一起每次走 1 步。快指针到 None 时，慢指针正好在「待删节点的前一个」，执行 slow.next = slow.next.next 即可。
#
# ---------- 关键点 ----------
# · 快指针先走 n+1 步，然后快慢一起每次走 1 步。这样快、慢之间始终隔着 n 个节点。当 fast 走到 None 时，slow 就在「倒数第 n 个」的前一个节点，执行 slow.next = slow.next.next 就删掉了倒数第 n 个。
# · 用哑节点 dummy 接在 head 前面：若倒数第 n 个正好是头节点，就没有前驱可改，用 dummy 当前驱就能统一处理。快慢都从 dummy 出发，fast 先走 n+1 步，这样 fast 到 None 时 slow 在 dummy，可以删 head。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
