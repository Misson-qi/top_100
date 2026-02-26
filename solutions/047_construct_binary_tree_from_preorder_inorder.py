# 力扣 热题100 · 第47题 从前序与中序遍历序列构造二叉树
# 链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# ---------- 思路 ----------
# 题目在问什么：给前序和中序遍历序列，还原二叉树。保证无重复值。
#
# 做法：前序第一个是根。在中序里找到根的位置，左边是左子树的中序、右边是右子树的中序；左子树节点数 = 中序里根左边的个数，据此把前序切成「左前序」「右前序」。递归用左前序+左中序建左子树，右前序+右中序建右子树。
#
# ---------- 关键点 ----------
# · 前序第一个是根。在中序里找到根的位置，左边是左子树的中序、右边是右子树的中序；左子树节点数 = 根在中序里的下标 - 左边界，所以前序里「根后面 left_len 个」是左子树前序，「再后面」是右子树前序。用下标 (pl, pr, il, ir) 传参，不用拷贝数组。
# · 用哈希表存「值→中序下标」，找根在中序里的位置 O(1)。递归出口：pl>pr 时返回 None。

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}

        def build(pl: int, pr: int, il: int, ir: int) -> Optional[TreeNode]:
            if pl > pr:
                return None
            root = TreeNode(preorder[pl])
            i = idx[root.val]
            left_len = i - il
            root.left = build(pl + 1, pl + left_len, il, i - 1)
            root.right = build(pl + left_len + 1, pr, i + 1, ir)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
