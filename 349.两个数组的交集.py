#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        intersec = []
        for num in set_nums2:
            if num in set_nums1:
                intersec.append(num)
        return intersec

        ## 法2
        return list(set(nums1) & set(nums2))

# @lc code=end

