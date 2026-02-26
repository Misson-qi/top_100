# 力扣 热题100 · 第28题 两数相加
# 链接: https://leetcode.cn/problems/add-two-numbers/
#
# ---------- 思路 ----------
# 题目在问什么：两条链表分别表示两个数的「个位→十位→百位…」，求两数之和，结果也用同样形式的链表表示。
#
# 做法：模拟竖式加法。用 carry 表示进位，同时从两链的个位（头节点）往后加。当前位 = (v1+v2+carry)%10，新进位 = (v1+v2+carry)//10。有一条链走完了就只加另一条和 carry，直到两条都走完且 carry 为 0。
#
# ---------- 关键点 ----------
# · 循环条件写成 l1 or l2 or carry：两条链都走完后，若还有进位（比如 9+9=18 最后一位要进 1），必须再建一个节点，所以 carry 不为 0 时还要进一次循环。
# · 每次先取当前位的和 v = carry，若 l1 存在就加上 l1.val 并 l1 后移，若 l2 存在就加上 l2.val 并 l2 后移，再用 v 除以 10 得到新进位和当前位。这样两链长度不同也能处理。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        p, carry = dummy, 0
        while l1 or l2 or carry:
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            carry, v = divmod(v, 10)
            p.next = ListNode(v)
            p = p.next
        return dummy.next
