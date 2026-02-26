# 力扣 热题100 · 第56题 子集
# 链接: https://leetcode.cn/problems/subsets/
#
# ---------- 思路 ----------
# 题目在问什么：给一个不重复的数组，返回所有子集（包括空集）。
#
# 做法：回溯。从下标 start 开始「可选集合」，每层先把当前 path 加入答案（这样每个子集都会在某一层被记录），再枚举 start 到 n-1，选一个数加入 path，递归 start 设为 i+1（保证不重复选、不重复子集），回溯时 pop。
#
# ---------- 关键点 ----------
# · 为什么每层一进来就先 ans.append(path[:])？因为进入这一层时，path 里已经是「当前考虑的一个子集」了。我们先把这个子集记下来，再枚举「这一层要选哪个数加进去」。这样，空集会在最开始 path 为空时被记录；选一个数、选两个数……都会在对应的层被记录，不会漏掉任何子集。
# · 为什么递归时下一层的 start 要传 i+1？因为我们约定「只从当前选的数的后面再选」，这样得到的子集里，元素在数组中的下标一定是递增的。比如只能出现 [nums[0], nums[2]]，不会出现 [nums[2], nums[0]]，否则就重复了（同一个子集被算两次）。所以每个子集只会被生成一次。

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start: int, path: List[int]) -> None:
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
