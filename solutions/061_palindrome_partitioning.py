# 力扣 热题100 · 第61题 分割回文串
# 链接: https://leetcode.cn/problems/palindrome-partitioning/
#
# ---------- 思路 ----------
# 题目在问什么：把字符串切成若干段，每段都是回文，求所有切法。
#
# 做法：回溯。从 start 开始，枚举结束位置 i，若 s[start:i+1] 是回文就加入 path，递归 dfs(i+1)，回溯时 pop。start 到末尾时把 path 加入答案。
#
# ---------- 关键点 ----------
# · 思路是「先决定第一段切到哪，再递归切剩下的」。从位置 start 开始，我们枚举「第一段的右端点」i（即第一段是 s[start:i+1]）。如果这一段是回文，就把它加入 path，然后递归处理「从 i+1 开始的后缀」；递归返回后把这一段从 path 里 pop 掉，再尝试下一个右端点。这样枚举了「第一段切 1 个字符、2 个字符、……」的所有情况，每种情况里剩下的部分再继续递归切，所以所有合法切法都会出现。
# · 回文判断：用双指针，一个从子串头、一个从子串尾往中间走，看是否都相等。若数据规模很大可以先用 DP 预处理出每段是否回文，本题直接判断即可。

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                ans.append(path[:])
                return
            for i in range(start, len(s)):
                if is_pal(start, i):
                    path.append(s[start : i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans
