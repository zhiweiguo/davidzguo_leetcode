#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        l = len(s)
        pre, cur = 1, 1
        for i in range(1, l):
            count = 0
            if s[i] > '0':
                count = cur
            if s[i-1] == '1' or (s[i-1]=='2' and s[i]<='6'):
                count += pre
            pre, cur = cur, count
        return cur


# @lc code=end

