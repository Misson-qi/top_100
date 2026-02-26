# 力扣 热题100 · 第70题 最小栈
# 链接: https://leetcode.cn/problems/min-stack/
#
# ---------- 思路 ----------
# 题目在问什么：实现栈，支持 push、pop、top，还要能 O(1) 得到当前栈里最小元素。
#
# 做法：一个栈存数据，另一个栈存「从底到当前」的最小值。push 时若 x 小于等于最小栈顶（或最小栈空）则最小栈也 push x；pop 时若数据栈顶等于最小栈顶则最小栈也 pop。getMin 取最小栈顶。
#
# ---------- 关键点 ----------
# · 用两个栈：一个正常存数据，另一个专门存「从栈底到当前为止的最小值」。push(x) 时，若 x 小于等于当前最小值（即最小栈的栈顶），说明新的最小值出现了，最小栈也要 push x；否则当前最小值没变，最小栈不动。这样最小栈的栈顶始终等于「当前数据栈里所有数的最小值」。pop 时，若弹出的数正好等于最小栈栈顶，说明弹掉的就是当前最小值，最小栈也要 pop 一次，这样新的栈顶就是「剩余数的最小值」。注意：当 x 等于当前最小值时也要压进最小栈，因为后面可能连续 pop 掉多个相同值，最小栈要弹同样次数才能对得上。

class MinStack:
    def __init__(self):
        self.st = []
        self.mn = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mn or val <= self.mn[-1]:
            self.mn.append(val)

    def pop(self) -> None:
        if self.st.pop() == self.mn[-1]:
            self.mn.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn[-1]
