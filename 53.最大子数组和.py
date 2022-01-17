#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     res = -2**32
    #     sums = 0
    #     for num in nums:
    #         sums += num
    #         if sums > res:
    #             res = sums
    #         if sums <= 0:
    #             sums = 0
    #     return res

    def maxSubArray(self, nums: List[int]) -> int:
        res = -2**32
        sums = 0
        for num in nums:
            if sums < 0:
                sums = num
            else:
                sums += num
            res = max(sums, res)
        return res


# @lc code=end

