#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# 贪心

# 采用了两次贪心的策略：
# 一次是从左到右遍历，只比较右边孩子评分比左边大的情况。
# 一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
# 这样从局部最优推出了全局最优，即：相邻的孩子中，评分高的孩子获得更多的糖果。

#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_arr = [1] * len(ratings) # 初始化
        # 从前向后遍历，判断与左边的相邻孩子的得分
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_arr[i] = candy_arr[i-1] + 1
        # 从后向前遍历，判断与右边相邻孩子的得分
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_arr[i] = max(candy_arr[i], candy_arr[i+1]+1)
        return sum(candy_arr)
# @lc code=end

