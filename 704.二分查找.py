#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    # # 法1: 左闭右闭
    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #     while left <= right:
    #         mid = left + (right-left)//2
    #         if nums[mid] > target:
    #             right = mid - 1
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             return mid
    #     return -1

    # 法2: 左闭右开
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)                   # 区别于1
        while left < right:                 # 区别于1
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


# @lc code=end

