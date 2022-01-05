#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        res = s[0]
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                res = s[i:j+1] if dp[i][j] and (j-i+1)>len(res) else res
        return res


                        

# @lc code=end






