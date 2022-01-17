#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1])) # 以身高从高到低排序(相同身高时，以x[1]较小者优先排于左边)
        res = []
        for p in people:
            res.insert(p[1], p)   # 按照p[1]的索引插入res队列中
        return res

# @lc code=end

