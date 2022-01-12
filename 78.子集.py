#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# 回溯

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]

#
# @lc code=start
class Solution:
    res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtracking(nums,[], 0)
        return self.res
    
    def backtracking(self, nums, path, start):
        self.res.append(path[:]) # 每次进入先把遍历到该层的结果添加到res中
        if start >= len(nums):
            return 
        for i in range(start, len(nums)):  # 层遍历
            path.append(nums[i])
            self.backtracking(nums, path, i+1)  # 层递归
            path.pop(-1)

# @lc code=end

