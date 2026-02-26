# 力扣 热题100 · 第58题 组合总和
# 链接: https://leetcode.cn/problems/combination-sum/
#
# ---------- 思路 ----------
# 题目在问什么：给正数数组和 target，找所有「和为 target」的组合，同一数可重复用，组合不重复（顺序不同算同一种按升序视为一种）。
#
# 做法：回溯。从下标 start 开始选数，当前和 cur。选 candidates[i] 时 path 加上、cur 加上，递归时 start 仍从 i 开始（可重复选）；cur==target 记录答案，cur>target 直接返回。回溯时 path 和 cur 恢复。
#
# ---------- 关键点 ----------
# · 同一个数可以重复用：所以选完 candidates[i] 之后，递归时 start 仍然传 i，下一层还可以再选 candidates[i]。这样就能得到 [2,2,3] 这种包含重复数的组合。
# · 怎么保证组合不重复（[2,3] 和 [3,2] 只算一种）？我们约定「只能从当前下标 start 往后选」，不能回头选前面的数。这样选出来的数在数组里的顺序一定是从左到右的，比如只会得到 [2,3]，不会得到 [3,2]。等价于「每个组合我们只按一种顺序生成」。
# · cur>target 时直接 return：因为都是正数，当前和已经超了，再往后加只会更大，不可能再凑出 target，所以不用再递归了，这叫剪枝。

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, path: List[int], cur: int) -> None:
            if cur == target:
                ans.append(path[:])
                return
            if cur > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, cur + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return ans
