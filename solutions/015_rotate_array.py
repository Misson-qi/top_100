# 力扣 热题100 · 第15题 轮转数组
# 链接: https://leetcode.cn/problems/rotate-array/
#
# ---------- 思路 ----------
# 题目在问什么：把数组「轮转」k 步，即最后 k 个数移到最前面，要求原地、O(1) 空间。
#
# 做法：三次反转。先把整个数组反转，再把前 k 个反转，再把后 n-k 个反转。结果就是后 k 个数跑到了前面且顺序正确。要先 k %= n，因为轮转 n 圈等于没转。
#
# ---------- 关键点 ----------
# · 三次反转：原数组可以看成 [前 n-k 个 | 后 k 个]。先整体反转，变成 [后 k 个的反转 | 前 n-k 个的反转]；再反转前 k 个、再反转后 n-k 个，就变成 [后 k 个正序 | 前 n-k 个正序]，正好是「后 k 个数移到前面」的轮转结果。
# · 先做 k %= n：轮转 n 圈等于没转；k 大于 n 时等价于 k%n。若 k==0 就直接 return，避免后面反转区间写错。

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return

        def rev(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)
