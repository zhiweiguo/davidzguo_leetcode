#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0
        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count += 1
            else:
                count -= 1
        return res
# @lc code=end

