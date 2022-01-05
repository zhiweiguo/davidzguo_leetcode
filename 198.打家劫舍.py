#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_1 = 0
        dp_2 = 0
        for i in range(len(nums)):
            dp_2, dp_1 = dp_1, max(dp_1, dp_2+nums[i])
        return dp_1
# @lc code=end

