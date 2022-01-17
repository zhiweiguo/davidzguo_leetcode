#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# 贪心

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        cur_dist = 0
        next_dist = 0
        for i in range(len(nums)-1):
            next_dist = max(nums[i]+i, next_dist) 
            if i == cur_dist:
                cur_dist = next_dist
                count += 1
        return count

# @lc code=end

