# 力扣 热题100 · 第25题 环形链表
# 链接: https://leetcode.cn/problems/linked-list-cycle/
#
# ---------- 思路 ----------
# 题目在问什么：判断链表里有没有环。要求 O(1) 空间（不能用哈希表存节点）。
#
# 做法：快慢指针。慢指针每次走 1 步，快指针每次走 2 步。若有环，快指针一定会从后面追上慢指针，两者相遇；若无环，快指针会先走到 None。
#
# ---------- 关键点 ----------
# · 有环时快指针一定会追上慢指针：快每次比慢多走 1 步，在环里相当于快在「追」慢，环长有限，所以一定会相遇。无环时快指针会先走到 None。
# · 循环要写 fast and fast.next：这样才会执行 fast.next.next，避免 fast 已经是 None 或只有一个节点时访问空指针。

from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
