#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if c > i:
                    continue
                dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != amount+1 else -1


# @lc code=end