#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left, right, top, down = 0, n-1, 0, n-1
        count = 1
        while left <= right and top <= down:
            for j in range(left, right+1):
                matrix[top][j] = count
                count += 1
            top += 1
            # if top > down:
            #     return matrix
            
            for i in range(top, down+1):
                matrix[i][right] = count
                count += 1
            right -= 1
            # if right < left:
            #     return matrix

            for j in range(right, left-1, -1):
                matrix[down][j] = count
                count += 1
            down -= 1
            # if down < top:
            #     return matrix

            for i in range(down, top-1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
            # if left > right:
            #     return matrix
        return matrix



# @lc code=end

