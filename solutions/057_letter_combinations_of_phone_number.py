# 力扣 热题100 · 第57题 电话号码的字母组合
# 链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
#
# ---------- 思路 ----------
# 题目在问什么：数字 2-9 对应若干字母，给一串数字，返回所有可能的字母组合（按数字顺序每位选一个字母）。
#
# 做法：回溯。当前处理到第 i 位，枚举 digits[i] 对应的每个字母 c，path+c 并递归 i+1；i 等于长度时说明组合完成，加入答案。
#
# ---------- 关键点 ----------
# · 思路是「第 1 位选一个字母，第 2 位选一个字母……」。当前处理到第 i 位（0 开始），digits[i] 是数字，用 mapping 查出对应的字母串（比如 "2"→"abc"）。枚举这个串里的每个字母 c，把 path+c 传给下一层递归，让下一层处理 i+1 位。这样就能枚举出所有组合。
# · path 用字符串，每次递归传 path+c，传下去的是新字符串，本层的 path 没被改过，所以返回后不需要像列表那样 pop 回溯。这是字符串不可变带来的方便。
# · 若 digits 是空串，不要调用 dfs，直接返回 []。否则 dfs("", 0) 会在一开始就发现 i==len(digits)，把空串 "" 加入答案，而题目一般要求空输入时返回空列表，不能含一个空字符串。

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        ans = []

        def dfs(path: str, i: int) -> None:
            if i == len(digits):
                ans.append(path)
                return
            for c in mapping[digits[i]]:
                dfs(path + c, i + 1)

        dfs("", 0)
        return ans
