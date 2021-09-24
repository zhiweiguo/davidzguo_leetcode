#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = {}
        for num in nums1:
            if num in nums1_count:
                nums1_count[num] += 1
            else:
                nums1_count[num] = 1
        intersec = []
        for num in nums2:
            if num in nums1_count and nums1_count[num] > 0:
                intersec.append(num)
                nums1_count[num] -= 1
        return intersec
# @lc code=end

