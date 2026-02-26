# 力扣 热题100 · 第72题 每日温度
# 链接: https://leetcode.cn/problems/daily-temperatures/
#
# ---------- 思路 ----------
# 题目在问什么：每天的温度，求每天要等几天才能遇到更高温度；没有则 0。
#
# 做法：单调栈（从底到顶对应温度递增）。从左到右遍历，当前温度若比栈顶对应温度高，说明栈顶那天「等到了」更高温度，答案为当前下标 - 栈顶下标，弹栈继续比；否则当前下标入栈。这样栈里是「还没等到更高温度」的下标。
#
# ---------- 关键点 ----------
# · 对每一天，我们要找「右边第一次比它热的那天」。用单调栈：栈里存的是「还没找到右边更大温度」的下标，且从栈底到栈顶，对应的温度是递增的。从左到右遍历，当遇到温度 temperatures[i] 比栈顶那天高时，说明栈顶那天「等到了」更高温度，且就是第 i 天，所以 ans[栈顶]=i-栈顶（间隔天数），然后弹栈继续看新的栈顶；当前 i 入栈。最后还在栈里的下标，说明右边没有更高温度，答案保持初始的 0 即可。

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans
