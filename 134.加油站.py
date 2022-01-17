#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    # # 暴力法
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     # 循环判断以每个数作为起始点时能否完成一圈
    #     for i in range(len(gas)):
    #         res = gas[i] - cost[i]
    #         idx = (i+1) % len(gas)
    #         # 以该点为七点，转一圈
    #         while res > 0 and idx != i: # res>=0时超时不通过
    #             res += gas[idx] - cost[idx]
    #             idx = (idx+1) % len(gas)
    #         # 完成一圈后若剩余油量不少于0且索引为i(说明完成了一圈),则返回该索引
    #         if res >= 0 and idx == i:
    #             return i
    #     return -1

    # # 贪心法1
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     rest = 0
    #     min_rest = 2**32
    #     # 遍历
    #     for i in range(len(gas)):
    #         rest += (gas[i] - cost[i]) # 记录截止到当前的剩余油量
    #         if rest < min_rest:   
    #             min_rest = rest  # 更新最小油量
    #     # case 1: 遍历完之后剩余油量<0,肯定不能跑够一圈,直接返回-1
    #     if rest < 0:  
    #         return -1
    #     # case 2: 遍历完之后最小的剩余油量>=0, 则0就满足
    #     if min_rest >= 0:  
    #         return 0
    #     # case 3: 遍历完之后剩余油量>=0,但是不能从0开始走，则找到能开始的位置
    #     for i in range(len(gas)-1, -1, -1): # 从后向前遍历
    #         min_rest += (gas[i] - cost[i])
    #         if min_rest >= 0: # 找到能把负数填平的点即为起始点
    #             return i
    #     return -1

    # 贪心法2
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = 0
        cur_rest = 0
        start = 0
        for i in range(len(gas)):
            rest += gas[i] - cost[i] # 整体的剩余量
            cur_rest += gas[i] - cost[i]  # 从start开始的剩余量
            if cur_rest < 0:  # 当前区间[start, i]剩余量为负时，肯定不能从该区间作为起始，更新起始位置为i+1
                start = i + 1
                cur_rest = 0  # 更新起始位置后，重置区间剩余量
        if rest < 0:
            return -1
        return start



# @lc code=end

