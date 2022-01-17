#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# 贪心

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l
        max_len = 1
        pre_diff = 0
        cur_diff = 0
        for i in range(1, l):
            cur_diff = nums[i] - nums[i-1]
            if (cur_diff>0 and pre_diff<=0) or (cur_diff<0 and pre_diff>=0):
                max_len += 1
                pre_diff = cur_diff
        return max_len




# @lc code=end

