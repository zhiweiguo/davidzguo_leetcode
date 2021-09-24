#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = {}
        for num in magazine:
            if num in mag_count:
                mag_count[num] += 1
            else:
                mag_count[num] = 1
        for num in ransomNote:
            if num in mag_count and mag_count[num] > 0:
                mag_count[num] -= 1
            else:
                return False
        return True

# @lc code=end

