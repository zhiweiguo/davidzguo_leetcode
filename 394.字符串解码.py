#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        stacks = []
        res = ''
        k = 0
        for c in s:
            if c.isdigit() :
                k = k*10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                stacks.append((k, res))
                k = 0
                res = ''
            elif c == ']':
                k_res_pair = stacks.pop(-1)
                res = k_res_pair[1]  + res * k_res_pair[0]
        return res
                    




# @lc code=end

