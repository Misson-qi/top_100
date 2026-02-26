# 力扣 热题100 · 第37题 二叉树的最大深度
# 链接: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
#
# ---------- 思路 ----------
# 题目在问什么：求二叉树从根到叶子的最长路径上的节点数（即最大深度）。
#
# 做法：递归。空树深度 0；否则当前深度 = 1 + max(左子树深度, 右子树深度)。
#
# ---------- 关键点 ----------
# · 以当前节点为根的「最大深度」= 1 + max(左子树最大深度, 右子树最大深度)。空树深度为 0。递归算左右子树深度，取较大者加 1 即可。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
