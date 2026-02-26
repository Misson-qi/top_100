# 力扣 热题100 · 第55题 全排列
# 链接: https://leetcode.cn/problems/permutations/
#
# ---------- 思路 ----------
# 题目在问什么：给一个不重复的数组，返回所有可能的全排列。
#
# 做法：回溯。用 path 记录当前排列，used 记录哪些数已用。每一层选一个还没用的数放进 path，递归下一层，返回后把该数从 path 去掉、used 还原。当 path 长度为 n 时说明排好了，把 path 的拷贝加入答案。
#
# ---------- 关键点 ----------
# · 为什么要 ans.append(path[:]) 而不是 ans.append(path)？因为 path 始终是同一个列表，后面回溯时会往 path 里加加减减。如果直接 append(path)，答案里存的是「指向这个列表的引用」，等回溯把 path 改乱了，你之前加进去的「排列」也会跟着变。用 path[:] 拷贝一份，存进去的就是当时的快照，不会被后面改动影响。
# · 怎么保证每个排列只出现一次？用 used 数组记「这个数有没有被选进当前 path」。每一层递归时，只从「还没用过」的数里选一个放进 path，然后 used[i]=True、递归下一层；递归返回后要把 used[i] 改回 False、并且 path.pop()，相当于「撤销这次选择」，这样才能尝试其它分支。枚举完所有「选谁放第一位、选谁放第二位……」的组合，就得到全部排列。

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ans = []

        def backtrack(path: List[int]) -> None:
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans
