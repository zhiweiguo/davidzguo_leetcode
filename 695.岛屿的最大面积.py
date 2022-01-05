#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    # dfs或bfs都可以，dp不可以，因为dp会出现重复统计的情况
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row*col == 0:
            return 0
        
        res = 0
        def dfs(grid, i, j):
            if i<0 or j<0 or i==row or j==col or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            num = 1
            for x,y in [[0,-1], [0,1], [-1,0], [1,0]]:
                num += dfs(grid, i+x, j+y)
            return num

        for i in range(row):
            for j in range(col):
                num = dfs(grid, i, j)
                res = max(res, num)
        return res


# @lc code=end

