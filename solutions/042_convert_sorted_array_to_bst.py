# 力扣 热题100 · 第42题 将有序数组转换为二叉搜索树
# 链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
#
# ---------- 思路 ----------
# 题目在问什么：给一个升序数组，构造一棵平衡的二叉搜索树（BST）。平衡指左右子树高度差不超过 1。
#
# 做法：每次取区间中点当根，左半区间递归建左子树，右半区间递归建右子树。这样左右节点数最多差 1，自然平衡；且左<根<右，满足 BST。
#
# ---------- 关键点 ----------
# · 每次取区间中点当根，左半区间递归建左子树、右半递归建右子树。这样左边都比根小、右边都比根大，满足 BST；且左右节点数最多差 1，树自然平衡。空数组时返回 None。

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1 :]),
        )
