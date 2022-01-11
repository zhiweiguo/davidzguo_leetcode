#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(res, path, 1, k, n)
        return res

    def backtracking(self, res, path, start, k, target):
        if target < 0:
            return
        if target == 0 and len(path) == k:
            res.append(path[:])
        while start <= 9:
            path.append(start)
            self.backtracking(res, path, start+1, k, target-start)
            path.pop(-1)
            start += 1
        
        
# @lc code=end

