# 力扣 热题100 · 第21题 搜索二维矩阵 II
# 链接: https://leetcode.cn/problems/search-a-2d-matrix-ii/
#
# ---------- 思路 ----------
# 题目在问什么：矩阵每行每列都升序，判断 target 是否在矩阵里。
#
# 做法：从右上角出发。当前值比 target 大说明这一列下面都更大，只能往左走；当前值比 target 小说明这一行左边都更小，只能往下走。等于就找到了。这样每次排除一行或一列，O(m+n)。
#
# ---------- 关键点 ----------
# · 从右上角开始：当前格子左边同行的都更小，下边同列的都更大。若当前值比 target 大，说明这一列下面都更大，只能往左走（j--）；若比 target 小，说明这一行左边都更小，只能往下走（i++）。每步都能排除一整行或一整列。
# · 为什么不能从左上角？左上角右边和下边都更大，当前比 target 大时不知道该往哪走。从右上或左下才有「一个方向变小、一个方向变大」，才能确定往哪走。

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
