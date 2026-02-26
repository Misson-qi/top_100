# 力扣 热题100 · 第8题 无重复字符的最长子串
# 链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
#
# ---------- 思路 ----------
# 题目在问什么：找一个最长的子串，里面没有重复的字符。
#
# 做法：滑动窗口。用 left、right 表示当前窗口 [left, right]，用 set 记录窗口里有哪些字符。right 往右扩，如果新字符已经在 set 里说明重复了，就从左边缩：不断 left++ 并把这个字符从 set 里删掉，直到没有重复为止；再把新字符加入 set。每次无重复时用窗口长度 right-left+1 更新答案。
#
# ---------- 关键点 ----------
# · 思路是枚举右端点 right，对每个 right 找「以 right 结尾的最长无重复子串」：左端点 left 要尽量小，但不能让 [left, right] 里出现重复字符。所以当 right 扩进一个新字符导致重复时，就要从左边缩：不断把 s[left] 从 set 里删掉并 left++，直到重复的那个字符被移出窗口为止。这样 [left, right] 又无重复了。
# · 每个字符最多进 set 一次、出 set 一次：right 只往右走，left 也只往右走（只在重复时缩），所以总复杂度 O(n)。
# · 用 set 记录「窗口里有哪些字符」就够了；左缩时一个一个删、left 一个一个加，直到重复消失。也可以用手写「字符→上次出现下标」一次把 left 跳到合适位置，但 set 写法更直观。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = ans = 0
        for right, c in enumerate(s):
            while c in seen:
                seen.discard(s[left])
                left += 1
            seen.add(c)
            ans = max(ans, right - left + 1)
        return ans
