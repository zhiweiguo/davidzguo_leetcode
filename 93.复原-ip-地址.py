#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

#  回溯

# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# @lc code=start
class Solution:
    res = []
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.backtracking(s, [], 0)
        return self.res
    
    def backtracking(self, s, path, start):
        if start >= len(s) and len(path) == 4:
            self.res.append('.'.join(path[:]))
            return 
        for i in range(start, len(s)):
            if self.isRight(s, start, i):
                path.append(s[start:i+1])
                self.backtracking(s, path, i+1)
                path.pop(-1)
 
    def isRight(self, s, start, end): 
        if start != end and s[start] == '0':
            return False
        if not s[start:end+1].isdigit:
            return False
        if int(s[start:end+1]) > 255:
            return False
        return True



# @lc code=end

