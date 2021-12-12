#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        res = []
        for c in s:
            if c in dic:
                res.append(dic[c])
            elif not res or c != res[-1]:
                return False
            else:
                res.pop(-1)
        return True if not res else False

# @lc code=end

