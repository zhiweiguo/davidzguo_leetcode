#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtracking(nums, [])
        return self.res
    
    def backtracking(self, nums, path):
        if len(path) == len(nums):
            self.res.append(path[:])
            return
        
        for num in nums:
            if num in path:
                continue
            path.append(num)
            self.backtracking(nums, path)
            path.pop(-1)


# @lc code=end

