#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
#    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         nums.sort()
#         n = len(nums)
#         res = []
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]: continue
#             for k in range(i+1, n):
#                 if k > i + 1 and nums[k] == nums[k-1]: continue
#                 p = k + 1
#                 q = n - 1

#                 while p < q:
#                     if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
#                     elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
#                     else:
#                         res.append([nums[i], nums[k], nums[p], nums[q]])
#                         while p < q and nums[p] == nums[p + 1]: p += 1
#                         while p < q and nums[q] == nums[q - 1]: q -= 1
#                         p += 1
#                         q -= 1
#         return res
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                                   
        return res

# @lc code=end

