#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回 s 所有可能的分割方案。

# 示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]

#

# @lc code=start
class Solution:
    res = []
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backtracking(s, [], int(0))
        return self.res

    def backtracking(self, s, path, start):
        if start >= len(s):
            self.res.append(path[:])
            return 
        for i in range(start, len(s), 1):
            if self.isPalindrome(s, start, i):
                path.append(s[start:i+1])
                self.backtracking(s, path, i+1)
                path.pop(-1)
            else: 
                continue

    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
# @lc code=end

