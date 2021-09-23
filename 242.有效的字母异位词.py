#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c)-ord('a')] += 1
        for c in t:
            char_count[ord(c)-ord('a')] -= 1
        for n in char_count:
            if n != 0:
                return False
        return True

# @lc code=end

