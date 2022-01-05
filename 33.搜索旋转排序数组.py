#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:     # 左边递增
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


# @lc code=end

