# 力扣 热题100 · 第50题 二叉树中的最大路径和
# 链接: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
#
# ---------- 思路 ----------
# 题目在问什么：找二叉树里「路径和」的最大值。路径是任意节点到任意节点，且只能沿父子边走，每个节点最多经过一次。
#
# 做法：对每个节点，若「最大路径」经过它，则路径 = 左子向下的一条链 + 当前节点 + 右子向下的一条链。DFS 返回「从该节点向下走到某叶子的最大单链和」（可含可不含子节点，取 max(0, 子返回值) 表示可以不要某侧）。在递归里用 左链+右链+节点值 更新全局答案。
#
# ---------- 关键点 ----------
# · 对每个节点，若「最大路径」经过它，路径 = 从左子某处上来 + 当前节点 + 往右子某处下去（即拐弯路径）。递归时返回「从该节点向下一条链」的最大和（给父节点用），用 max(0, 子) 表示可以不要某侧（避免负的拉低）。在递归里用 左链+右链+节点值 更新全局答案。
# · 返回值是 node.val + max(左链, 右链)：因为给父节点用的只能是「从当前节点往下的一条链」，不能同时走左右两边，否则就不是一条链了。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0
            L = max(0, gain(node.left))
            R = max(0, gain(node.right))
            ans = max(ans, node.val + L + R)
            return node.val + max(L, R)

        gain(root)
        return ans
