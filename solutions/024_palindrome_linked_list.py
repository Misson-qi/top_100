# 力扣 热题100 · 第24题 回文链表
# 链接: https://leetcode.cn/problems/palindrome-linked-list/
#
# ---------- 思路 ----------
# 题目在问什么：判断一条链表是不是回文（正着读和反着读一样）。要求 O(n) 时间、O(1) 空间。
#
# 做法：快慢指针找到中点（或偏右），把后半段链表反转，然后前半段头指针和后半段头指针一起往右走，逐个比较值。都一样就是回文。偶数个节点时前后半段等长；奇数个时后半段多一个中点，比较时后半段会多走一步，但前半段走完就停即可。
#
# ---------- 关键点 ----------
# · 用快慢指针找中点：slow 每次一步、fast 每次两步，fast 走完时 slow 在中点（偶数个时是后半段第一个）。从 slow 开始把后半段链表反转，得到的新头是 prev。前半段头是 head，后半段反转后头是 prev，两个指针一起往右走，逐个比较值是否相等；奇数个时前半段会多一个中点，比较时以后半段为准，前半段走完就停。
# · 若题目要求不修改链表，比较完可以把后半段再反转回去并接好；若允许修改，可以不恢复。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
