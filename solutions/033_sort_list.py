# 力扣 热题100 · 第33题 排序链表
# 链接: https://leetcode.cn/problems/sort-list/
#
# ---------- 思路 ----------
# 题目在问什么：给链表排序，要求 O(n log n) 时间、尽量省空间（递归栈 O(log n) 可接受）。
#
# 做法：归并排序。用快慢指针找中点，把链表从中间断开，递归排序前半段和后半段，再把两条有序链表合并成一条（和「合并两个有序链表」一样）。
#
# ---------- 关键点 ----------
# · 用快慢指针找中点：让 fast 从 head.next 开始（而不是 head），这样偶数个节点时 slow 停在中点前一个，取 mid=slow.next 作为后半段头，slow.next=None 断开。递归排序前半段和后半段，再用「合并两个有序链表」的方法合并。
# · 递归出口：head 为空或只有一个节点时直接返回。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        dummy = ListNode(0)
        p = dummy
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left or right
        return dummy.next
