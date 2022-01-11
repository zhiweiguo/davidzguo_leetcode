#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtracking(path, start):
            l = len(path)
            if l == k:
                res.append(path[:])  # 直接使用path为空
                return
            while start <= n:
                path.append(start)
                backtracking(path, start+1)
                path.pop(-1)
                start += 1

        backtracking(path, 1)
        return res
            

    
# @lc code=end

