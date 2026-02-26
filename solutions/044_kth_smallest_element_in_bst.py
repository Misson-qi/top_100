# 力扣 热题100 · 第44题 二叉搜索树中第 K 小的元素
# 链接: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
#
# ---------- 思路 ----------
# 题目在问什么：在 BST 里找第 k 小的元素（1-indexed）。BST 中序遍历是升序，所以第 k 个就是答案。
#
# 做法：用栈做中序遍历（左-根-右）。每次弹栈访问一个节点就 k--，k 变 0 时该节点值就是答案，直接返回。
#
# ---------- 关键点 ----------
# · BST 的中序遍历是升序，所以「第 k 个被访问的节点」就是第 k 小。用栈做迭代中序，每弹栈访问一个节点就 k--，k 变成 0 时当前节点就是答案，直接返回。k 小的话可能不用遍历整棵树，但最坏仍要 O(n)。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return 0
