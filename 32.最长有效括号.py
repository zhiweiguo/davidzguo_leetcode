#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        l = len(s)
        stack = [-1]
        max_num = 0
        for i in range(l):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_num = max(max_num, i-stack[-1])
        return max_num
        
# @lc code=end

