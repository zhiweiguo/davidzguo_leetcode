#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            # 只找到每天相比于前一天盈利的情况（局部最优），最后相加即可（全局最优）
            res += max(prices[i]-prices[i-1], 0)
        return res

    # 动态规划
    #def maxProfit(self, prices: List[int]) -> int:

# @lc code=end

