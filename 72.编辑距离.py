#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    left = dp[i][j-1] + 1
                    up = dp[i-1][j] + 1
                    left_up = dp[i-1][j-1]
                    if word1[i-1] != word2[j-1]:
                        left_up += 1
                    dp[i][j] = min(left, up, left_up)
        return dp[-1][-1]
# @lc code=end

