# 力扣 热题100 · 第38题 翻转二叉树
# 链接: https://leetcode.cn/problems/invert-binary-tree/
#
# ---------- 思路 ----------
# 题目在问什么：把二叉树每个节点的左右子对调，得到镜像树。
#
# 做法：递归。先递归翻转左子树、右子树，再交换当前节点的 left 和 right，返回当前根。
#
# ---------- 关键点 ----------
# · 先递归翻转左子树、右子树，再交换当前节点的 left 和 right。这样从叶子往上，每个节点只做一次交换，整棵树就左右镜像了。
# · 也可以一行写：root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)，即先得到翻转后的右子树和左子树，再对调赋给 left 和 right。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
