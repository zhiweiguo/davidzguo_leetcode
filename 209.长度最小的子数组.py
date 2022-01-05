#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    # 滑动窗口
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        sub_sum = 0
        sub_len = 2**32
        for i in range(len(nums)):
            sub_sum += nums[i]
            while sub_sum >= target:
                sub_len = min(sub_len, i-start+1)
                sub_sum -= nums[start]
                start += 1
        return 0 if sub_len == 2**32 else sub_len

        
# @lc code=end

