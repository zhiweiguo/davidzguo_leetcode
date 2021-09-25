#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sums_set = set()
        num = n
        while True:
            sums = 0
            for c in str(num):
                sums += int(c)**2
            if sums == 1:
                return True
            elif sums in sums_set:
                return False
            else:
                sums_set.add(sums)
            num = sums
            


# @lc code=end

