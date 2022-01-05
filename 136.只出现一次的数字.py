#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if n not in res:
                res.append(n)
            else:
                res.remove(n)
        return res[0]
# @lc code=end

