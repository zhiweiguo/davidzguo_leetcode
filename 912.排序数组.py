#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[i] = nums[i], nums[pivot]

            quick(left, j-1)
            quick(j+1, right)

            return nums

        return quick(0, n-1) 

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     l = len(nums)
    #     if l <2:
    #         return nums       
    #     pivot = self.partion(nums)
    #     if pivot > 1:
    #         nums[:pivot] = self.sortArray(nums[:pivot])
    #     if pivot < l-2:
    #         nums[pivot+1:] = self.sortArray(nums[pivot+1:])
            
    #     return nums


    # def partion(self, nums):
    #     pivot = nums[0]
    #     left = 0
    #     right = len(nums) - 1
    #     while left < right:
    #         while left < right and nums[right] > pivot:
    #             right -= 1
    #         nums[left] = nums[right]
    #         while left < right and nums[left] <= pivot:
    #             left += 1
    #         nums[right] = nums[left]
    #     nums[left] = pivot
    #     return left

        


# @lc code=end

