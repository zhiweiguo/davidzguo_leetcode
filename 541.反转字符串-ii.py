#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        l = len(s)
        i = 2
        while i*k < l:
            s[(i-2)*k:(i-1)*k] = self._reverse(s[(i-2)*k:(i-1)*k])
            i += 2
        end = min(l, (i-1)*k)
        s[(i-2)*k:end] = self._reverse(s[(i-2)*k:end])
        return ''.join(s)


    def _reverse(self, s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

# @lc code=end

