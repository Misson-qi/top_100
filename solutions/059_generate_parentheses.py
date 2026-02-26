# 力扣 热题100 · 第59题 括号生成
# 链接: https://leetcode.cn/problems/generate-parentheses/
#
# ---------- 思路 ----------
# 题目在问什么：生成所有由 n 对括号组成的、且合法的括号序列。
#
# 做法：回溯。维护当前已有的左、右括号个数。还能加左括号时（left<n）就加 '(' 并递归；还能加右括号时（right<left，保证左不少于右才加右）就加 ')' 并递归。长度到 2n 时加入答案。
#
# ---------- 关键点 ----------
# · 合法括号序列的要求：从左往右数，任意位置左括号的数量都不能少于右括号（否则就有「先闭后开」的不合法情况）。所以我们在生成时，只有「当前右括号个数小于左括号个数」时才能加 ')'；左括号只要还没到 n 个就可以加 '('。这样生成出来的序列一定合法。
# · 为什么这样能不重不漏？每一步要么加 '('（当 left<n），要么加 ')'（当 right<left），我们按顺序尝试所有可能。每个合法的 n 对括号序列，都对应唯一一条「在每一步做了哪种选择」的路径，所以每个合法序列会被生成恰好一次。

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path: str, left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append(path)
                return
            if left < n:
                backtrack(path + "(", left + 1, right)
            if right < left:
                backtrack(path + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans
