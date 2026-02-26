# 力扣 热题100 · 第31题 K 个一组翻转链表
# 链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/
#
# ---------- 思路 ----------
# 题目在问什么：把链表每 k 个节点为一组进行反转，不足 k 个的保持不动。
#
# 做法：用 pre 指向「当前这一段」的前驱。每次从 pre 往后走 k 步得到这段的尾 tail，若不足 k 个就结束。把 [pre.next, tail] 这一段反转（写一个 reverse(head, tail) 返回新的头、尾），把 pre 接到新头、新尾接到下一段的头，然后 pre 移到新尾；重复直到不足 k 个。
#
# ---------- 关键点 ----------
# · 写一个 reverse(head, tail)：把从 head 到 tail 这一段反转，且让反转后的尾（原 head）指向 tail 原来的 next，这样不断链。做法是 prev 初值设为 tail.next，然后像普通反转链表一样把这段反完，返回 (新头, 新尾) = (tail, head)。
# · 每次从 pre 往后走 k 步得到 tail；若走不满 k 步就遇到 None，说明剩余不足 k 个，直接返回。反转完当前段后，把 pre 接到新头、新尾接到下一段头，然后 pre 移到新尾（即下一段的前驱）。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        def reverse(head: ListNode, tail: ListNode):
            prev = tail.next
            cur = head
            while prev != tail:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return tail, head

        dummy = ListNode(0, head)
        pre = dummy
        while True:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt_start = tail.next
            new_head, new_tail = reverse(pre.next, tail)
            pre.next = new_head
            new_tail.next = nxt_start
            pre = new_tail
