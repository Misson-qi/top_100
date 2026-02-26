# 力扣 热题100 · 第64题 搜索二维矩阵
# 链接: https://leetcode.cn/problems/search-a-2d-matrix/
#
# ---------- 思路 ----------
# 题目在问什么：每行有序且下一行首大于上一行末，整体可视为一维升序，判断 target 是否在矩阵中。
#
# 做法：把二维当一维有序数组做二分。总长度 m*n，mid 对应二维下标 (mid//n, mid%n)。按一维二分比较 matrix[mid//n][mid%n] 与 target 即可。
#
# ---------- 关键点 ----------
# · 题目条件保证了：把矩阵按行依次拼成一维数组后，这个一维数组是严格升序的。所以我们可以「假装」有一个长度为 m*n 的一维数组，对它做二分。一维下标 k 对应二维坐标 (k//n, k%n)：比如 n=4 时，k=0,1,2,3 对应第 0 行，k=4,5,6,7 对应第 1 行……所以 mid 对应的元素是 matrix[mid//n][mid%n]。按普通二分比较这个元素和 target 即可。

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
