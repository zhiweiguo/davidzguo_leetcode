#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    # 栈
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:
                res.pop(-1)
            else:
                res.append(c)
        return "".join(res)

#    # 快慢指针 
#     def removeDuplicates(self, s):
#         slow = fast = 0
#         l = len(s)
#         res = list(s)
#         while fast < l:
#             res[slow] = res[fast]
#             if slow > 0 and res[slow] == res[slow-1]:
#                 slow -= 1
#             else:
#                 slow += 1
#             fast += 1
#         return "".join(res[:slow])
# @lc code=end

