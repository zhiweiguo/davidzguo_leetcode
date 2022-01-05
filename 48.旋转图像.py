#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        # 主对角线翻转（左上到右下对应的对角线）
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


# @lc code=end

