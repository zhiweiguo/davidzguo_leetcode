#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for t in tokens:
            if t == "+":
                a = res.pop(-1)
                b = res.pop(-1)
                res.append(a+b)
            elif t == "-":
                a = res.pop(-1)
                b = res.pop(-1)
                res.append(b-a)
            elif t == "*":
                a = res.pop(-1)
                b = res.pop(-1)
                res.append(a*b)
            elif t == "/":
                a = res.pop(-1)
                b = res.pop(-1)
                res.append(int(b/a)) # 不能是//，int()是向0取整, //是向小的方向取整
            else:
                res.append(int(t))
        return res.pop(-1)
# @lc code=end

