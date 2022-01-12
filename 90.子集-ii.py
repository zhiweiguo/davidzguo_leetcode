#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# 回溯

# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1,2,2]
# 输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]
#

# @lc code=start
class Solution:
    res = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort() # 排序很关键
        self.backtracking(nums,[], 0)
        return self.res
    
    def backtracking(self, nums, path, start):
        self.res.append(path[:]) # 每次进入先把遍历到该层的结果添加到res中
        if start >= len(nums):
            return 
        for i in range(start, len(nums)):  # 层遍历
            if  i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, path, i+1)  # 层递归
            path.pop(-1)
# @lc code=end

