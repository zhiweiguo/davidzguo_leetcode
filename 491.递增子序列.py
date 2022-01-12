#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# 回溯

# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

# 示例:

# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:

# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#

# @lc code=start
class Solution:
    res = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtracking(nums, [], 0)
        return self.res

    def backtracking(self, nums, path, start):
        if len(path) >= 2:
            self.res.append(path[:])
        used = [] # 记录该层使用过的元素
        for i in range(start, len(nums)):
            # path不为空且当前值小于path最后一个值时不考虑
            # 当前值在该层已经使用过时不考虑
            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue
            used.append(nums[i])
            path.append(nums[i])
            self.backtracking(nums, path, i+1)   # 递归到下一层
            path.pop(-1)
    

# @lc code=end

