#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        res = 0
        idx = 0
        max_idx = 0
        while idx <= max_idx:
            # 得到当前位置能到达的最远位置
            max_idx = max(max_idx, idx + nums[idx])
            # 如果能到达的最远距离已经覆盖到最后一个位置，则立即返回
            if max_idx >= l-1:
                return True
            idx += 1
        
        return max_idx >= l-1
# @lc code=end

