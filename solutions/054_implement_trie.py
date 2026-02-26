# 力扣 热题100 · 第54题 实现 Trie (前缀树)
# 链接: https://leetcode.cn/problems/implement-trie-prefix-tree/
#
# ---------- 思路 ----------
# 题目在问什么：实现前缀树。insert 插入一个单词；search 查单词是否在树里；startsWith 查是否有以某前缀开头的单词。
#
# 做法：每个节点有 children（字符→下一节点）和 is_end（是否有一个单词在这里结束）。insert：沿单词每个字符走，没有就建节点，最后把终点标 is_end。search：沿路径走到底，看终点是否 is_end。startsWith：沿路径走到底，能走完就说明有该前缀。
#
# ---------- 关键点 ----------
# · 前缀树像一棵「按字母往下走」的树：根节点不存字符，从根出发，每条边代表一个字符。比如插 "apple" 就是根→a→p→p→l→e，每个节点用 children 字典存「下一个字符 → 下一个节点」。最后一个字母的节点要标 is_end=True，表示有一个单词在这里结束（否则 "app" 和 "apple" 会混在一起）。
# · search("apple")：从根沿 a→p→p→l→e 走，走完后要看终点节点的 is_end 是不是 True。若是 True 说明树里存了完整单词 "apple"；若只是路径存在但 is_end 是 False，说明只存了 "app" 之类的前缀，没有存 "apple" 这个完整单词。
# · startsWith("app")：只要从根能沿 a→p→p 走完这条路径就行，不需要终点是单词结尾。所以走完后不用看 is_end，能走完就返回 True。

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_end = True

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True
