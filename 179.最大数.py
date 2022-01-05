#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a+b == b+a:
                return 0
            elif a+b > b+a:
                return 1
            else:
                return -1
        
        def quick_sort(nums, start, end):
            if start >= end:
                return 
            partion_idx = partion(nums, start, end)
            
            quick_sort(nums, start, partion_idx-1)
            quick_sort(nums, partion_idx+1, end)
            
        def partion(nums, start, end):
            partion_v = nums[start]
            while start < end:
                while start < end and compare(nums[end], partion_v) == -1:
                    end -= 1
                nums[start] = nums[end]
                while start < end and compare(nums[start], partion_v) >= 0:
                    start += 1
                nums[end] = nums[start]
            nums[start] = partion_v
            return start

        if len(nums) == 0:
            return ''
        if max(nums) == 0:
            return '0'
        nums = [str(n) for n in nums]
        quick_sort(nums, 0, len(nums)-1)
        return ''.join(nums)


# @lc code=end

