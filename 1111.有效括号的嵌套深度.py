#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        deep = 0
        for i in range(len(seq)):
            if seq[i] == '(':
                deep += 1
                res.append(deep%2)
            else:
                res.append(deep%2)
                deep -= 1
        return res
        
# @lc code=end

