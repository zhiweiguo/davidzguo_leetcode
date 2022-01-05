#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums):
        dp_2, dp_1 = 0, 0
        for i in range(len(nums)):
            dp_2, dp_1 = dp_1, max(dp_1, dp_2+nums[i])
        return dp_1
# @lc code=end

