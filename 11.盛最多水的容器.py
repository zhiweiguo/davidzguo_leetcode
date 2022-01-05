#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # 双指针
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l <=1:
            return 0
        left = 0
        right = l - 1
        res = 0
        while left < right:
            res = max(min(height[right],height[left])*(right-left), res)
            if height[left]<= height[right]:
                left += 1
            else:
                right -= 1
        return res
        
# @lc code=end

