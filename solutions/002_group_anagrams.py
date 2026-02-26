# 力扣 热题100 · 第2题 字母异位词分组
# 链接: https://leetcode.cn/problems/group-anagrams/
#
# ---------- 思路 ----------
# 题目在问什么：把「字母相同、顺序不同」的字符串分到同一组（例如 "eat" 和 "tea" 是同一组）。
#
# 核心想法：给每组定一个「统一代表」。两个字符串要是同一组，它们的「代表」必须相同。
# 最简单的代表：把字符串里的字母排个序。例如 "eat" → "aet"，"tea" → "aet"，所以 "eat" 和 "tea" 会得到同一个 key。
# 用字典：key = 这个代表（排序后的字符串或元组），value = 所有属于这一组的原字符串组成的列表。
# 遍历每个字符串，算它的 key，把它放进字典里对应的列表；最后把字典里所有列表拿出来就是答案。
#
# ---------- 关键点 ----------
# · 为什么用「排序后的字符串」当代表？异位词就是字母种类和个数一样、顺序可以不同。排序后同一组的都会变成同一串（比如 "eat" 和 "tea" 都变成 "aet"），不同组的字母组成不同，排序后一定不一样。所以用排序结果当 key，和「组」是一一对应的。
# · 当 key 要用 tuple(sorted(s))：Python 里字典的 key 必须可哈希，list 不能当 key，tuple 可以。sorted(s) 得到的是 list，所以要转成 tuple 再放进字典。
# · 也可以把每个字母出现次数存成长 26 的元组当 key，能区分组，但写起来麻烦；排序写法简单，一般就够用了。

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())
