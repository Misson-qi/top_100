# 力扣 热题100 · 第41题 二叉树的层序遍历
# 链接: https://leetcode.cn/problems/binary-tree-level-order-traversal/
#
# ---------- 思路 ----------
# 题目在问什么：按层输出二叉树的值，每一层单独一个列表，从左到右。
#
# 做法：BFS 用队列。先把根入队。每次循环时，当前队列长度就是这一层的节点数，按这个次数弹节点，把值放进这一层的列表，并把每个节点的左右子（非空）入队。队列空时结束。
#
# ---------- 关键点 ----------
# · 每一轮开始前先取 len(q)，用 for _ in range(len(q)) 只弹「当前层」这么多节点。因为弹一个节点会把它的左右子入队，若不限制次数，就会把下一层的也一起弹完。先记下「这一层有多少个」再弹，弹完时新入队的全是下一层，下一轮再处理。

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row)
        return ans
