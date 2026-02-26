# 力扣 热题100 · 第71题 字符串解码
# 链接: https://leetcode.cn/problems/decode-string/
#
# ---------- 思路 ----------
# 题目在问什么：形如 "3[a2[c]]" 展开成 "accaccacc"，即数字表示后面方括号内串重复次数。
#
# 做法：栈。遇到数字就拼成 k；遇到 '[' 把 (当前串, k) 压栈并重置当前串和 k；遇到 ']' 弹栈得到 (前缀, k)，当前串 = 前缀 + 当前串重复 k 次。字母直接拼到当前串。
#
# ---------- 关键点 ----------
# · 遇到 '[' 表示进入一层括号：这时要把「当前已经拼好的字符串」和「这个括号前面的数字 k」记下来压栈，然后把 cur 和 k 清空。因为方括号里的内容要单独拼，拼完再按前面的数字重复 k 次。遇到 ']' 表示这一层括号结束：弹栈得到 (前缀, n)，当前 cur 就是括号里拼好的内容，把它重复 n 次接到「前缀」后面，得到新的 cur（相当于把这一层展开完了，交回给上一层）。数字可能不止一位，比如 "12["，要边读边用 k=k*10+int(c) 累积，等读到 '[' 时再用这个 k。

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cur, k = "", 0
        for c in s:
            if c == "[":
                st.append((cur, k))
                cur, k = "", 0
            elif c == "]":
                pre, n = st.pop()
                cur = pre + cur * n
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                cur += c
        return cur
