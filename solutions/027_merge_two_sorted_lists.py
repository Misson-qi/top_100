# 力扣 热题100 · 第27题 合并两个有序链表
# 链接: https://leetcode.cn/problems/merge-two-sorted-lists/
#
# ---------- 思路 ----------
# 题目在问什么：把两条已经按值升序的链表合并成一条升序链表。
#
# 做法：用一个哑节点 dummy 当新链表的头，用指针 p 指向当前新链的尾巴。每次比较 list1 和 list2 的头节点，把小的那个接到 p 后面，然后 p 和该链的指针后移。有一条用完就把另一条剩余部分整体接到 p 后面。
#
# ---------- 关键点 ----------
# · 用哑节点 dummy 当新链的头，p 指向当前新链的尾巴。每次比较两条链当前节点，把小的接到 p 后面，p 和该链的指针后移。这样不用单独处理「第一个节点」。
# · 有一条链走完后，把另一条链剩下的部分整段接到 p 后面即可，因为本来就是有序的。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        p.next = list1 or list2
        return dummy.next
