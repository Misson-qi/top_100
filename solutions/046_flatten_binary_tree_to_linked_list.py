# 力扣 热题100 · 第46题 二叉树展开为链表
# 链接: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
#
# ---------- 思路 ----------
# 题目在问什么：把二叉树按「前序遍历顺序」展开成只有右子指针的链表，原地修改。
#
# 做法：递归。先递归 flatten 左、右子树。然后把「已经展平的左链」接到根的右边；再顺着这条链走到末尾，把「已经展平的右链」接上去；最后把根的 left 置空。
#
# ---------- 关键点 ----------
# · 用后序：先递归 flatten 左、右子树（它们已经变成「根-右-右-...」的一条链）。然后把展平后的左子树接到 root 的右边（root.right = left），再顺着 root 一直往右走到链尾，把展平后的右子树接上去，最后 root.left = None。这样顺序就是 根-左子树展平-右子树展平，即前序遍历顺序。
# · 找「左链」的尾：接完 left 后 root.right 就是左链的头，从 root 一直 .right 走到没有下一个，那个节点就是左链尾，再把原来的右子树接上去。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        left, right = root.left, root.right
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right
