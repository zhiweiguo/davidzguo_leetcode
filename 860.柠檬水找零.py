#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_count = {5: 0, 10: 0, 20: 0}  # 直接用变量存也行
        for bill in bills:
            if bill == 5:
                change_count[5] += 1
            elif bill == 10:
                if change_count[5] < 1:
                    return False
                change_count[5] -= 1
                change_count[10] += 1
            elif bill == 20:
                if change_count[10] >= 1 and change_count[5] >= 1:
                    change_count[10] -= 1
                    change_count[5] -= 1
                    change_count[20] += 1
                elif change_count[10] < 1 and change_count[5] >= 3:
                    change_count[5] -= 3
                    change_count[20] += 1
                else:
                    return False
        return True
# @lc code=end

