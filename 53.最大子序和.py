#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = cur_sum + nums[i] if cur_sum > 0 else nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum

# @lc code=end

