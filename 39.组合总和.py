#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]

# 示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]

#

# @lc code=start
class Solution:
    res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtracking(candidates, [], 0, target)
        return self.res
    
    def backtracking(self, candidates, path, start, target):
        if target < 0:
            return
        if target == 0:
            self.res.append(path[:])
            return 
        # start不能小于上一层的start位置
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, path, i, target-candidates[i])
            path.pop(-1)

# @lc code=end

