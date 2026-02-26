# 力扣 热题100 · 第22题 相交链表
# 链接: https://leetcode.cn/problems/intersection-of-two-linked-lists/
#
# ---------- 思路 ----------
# 题目在问什么：两条链表可能在某节点之后合并成一条，找这个「交点」；没有交点返回 None。要求 O(1) 空间。
#
# 做法：两个指针 pa、pb 分别从 headA、headB 出发，每次各走一步。谁先走到 None 就接到另一条链表的头继续走。若两链相交，设 A 独有 a 个、B 独有 b 个、公共段 c 个，则 pa 走 a+c+b、pb 走 b+c+a，长度相同，会在交点相遇；若不相交，会同时走到 None。
#
# ---------- 关键点 ----------
# · 两个指针分别从两条链的头出发，每次各走一步；谁先走到链尾 None 就接到另一条链的头继续走。这样 pa 走的相当于「链A + 链B」，pb 走的相当于「链B + 链A」，总长度一样。若相交，它们会在公共段上相遇（即交点）；若不相交，会同时走到 None。
# · 为什么相交时一定在交点相遇？设链A 独有 a 个节点、链B 独有 b 个、公共段 c 个。pa 走完 a+c 再走 b 步、pb 走完 b+c 再走 a 步时，都在公共段上且步数相同，所以一定同时走到公共段的第一个节点，也就是交点。

from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
