#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)
        l = len(nums)
        idx = 0
        for i in range(l):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        # # 法1,直接计算
        # if k > 0:
        #     nums[-1] *= (-1)**k
        
        # 法2, k为奇数，则反转；k为偶数，则保持不变
        if k % 2 == 1:
            nums[-1] = -nums[-1]
        return sum(nums)
# @lc code=end

