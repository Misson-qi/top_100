# 力扣 热题100 · 第43题 验证二叉搜索树
# 链接: https://leetcode.cn/problems/validate-binary-search-tree/
#
# ---------- 思路 ----------
# 题目在问什么：判断一棵树是不是二叉搜索树（BST）：左子树所有值 < 根 < 右子树所有值，且左右子树也是 BST。
#
# 做法：递归时传「当前节点值允许的范围」(lower, upper)。根必须在 (lower, upper) 内；左子树范围 (lower, root.val)，右子树范围 (root.val, upper)。根用负无穷到正无穷。
#
# ---------- 关键点 ----------
# · 只判断「左子<根<右子」不够：左子树里可能某个孙节点比根大。所以递归时要传「当前子树允许的取值范围」(lo, hi)：根必须在 (lo, hi) 内，左子树范围 (lo, root.val)，右子树范围 (root.val, hi)。这样从上往下传约束，整棵左子树都 < 根、整棵右子树都 > 根。根节点用 (-inf, +inf)；空节点算合法。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ok(node: Optional[TreeNode], lo: float, hi: float) -> bool:
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)

        return ok(root, float("-inf"), float("inf"))
