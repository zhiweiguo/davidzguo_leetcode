#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            res = max(prices[i]-min_price, res)
            min_price = min(min_price, prices[i])
        return res
# @lc code=end

