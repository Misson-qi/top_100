# 力扣 热题100 · 第68题 寻找两个正序数组的中位数
# 链接: https://leetcode.cn/problems/median-of-two-sorted-arrays/
#
# ---------- 思路 ----------
# 题目在问什么：两个有序数组合并后的中位数（若总长为偶数为两中间数的平均）。要求 O(log(m+n))。
#
# 做法：在较短数组上二分「分割点」i。设 A 左边有 i 个、B 左边有 j 个，令 i+j = (m+n+1)//2（左半个数）。满足「左半最大值 <= 右半最小值」时，中位数由左半最大和右半最小得到。二分找满足条件的 i。
#
# ---------- 关键点 ----------
# · 为什么在「短数组」上二分：我们令 j = (m+n+1)//2 - i。i 的范围是 [0, m]，要保证 j 在 [0, n] 内。若在长数组上二分，i 可能取到很大，j 会变成负数。所以先 if len(nums1)>len(nums2) 交换，保证 A 是短的那个，在 A 上二分 i，j 自然合法。
# · 左半取 (m+n+1)//2 个：这样总长度为奇数时，中位数就是「左半的最大值」；偶数时左半比右半多 1 或相等，中位数 = (左半最大 + 右半最小) / 2。用 (m+n+1)//2 可以统一写成「左半最大」和「右半最小」。
# · 合法分割条件：左半最大值 <= 右半最小值。即 max(A[i-1], B[j-1]) <= min(A[i], B[j])，拆开就是 A[i-1]<=B[j] 且 B[j-1]<=A[i]。不满足时：若 A[i-1] > B[j]，说明 A 左半取多了，i 要变小（hi=i-1）；否则 A 左半取少了，lo=i+1。
# · 边界 i=0、i=m、j=0、j=n：用 ±inf 表示「没有左边元素」或「没有右边元素」，这样不用单独分支，比较时不会越界。例如 i=0 时 max_left_a 用 -inf，表示 A 左边没有，左半最大只来自 B。

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            max_left_a = nums1[i - 1] if i else float("-inf")
            min_right_a = nums1[i] if i < m else float("inf")
            max_left_b = nums2[j - 1] if j else float("-inf")
            min_right_b = nums2[j] if j < n else float("inf")
            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                left_max = max(max_left_a, max_left_b)
                if (m + n) % 2 == 1:
                    return float(left_max)
                right_min = min(min_right_a, min_right_b)
                return (left_max + right_min) / 2.0
            if max_left_a > min_right_b:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0
