#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        n_2 = 1
        n_1 = 2
        for i in range(3, n+1):
            n_2, n_1 = n_1, n_1 + n_2
        return n_1
# @lc code=end

