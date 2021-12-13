#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Mydeque:
    def __init__(self):
        self.deque = []
    def push(self, v):
        while self.deque and self.deque[-1] < v:
            self.deque.pop(-1)
        self.deque.append(v)
    def pop(self, v):
        if self.deque and self.deque[0] == v:
            self.deque.pop(0)
    def max(self):
        return self.deque[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_deque = Mydeque()
        res = list()
        for i in range(len(nums)):
            if i < k-1:
                my_deque.push(nums[i])
            else:
                my_deque.push(nums[i])
                res.append(my_deque.max())
                my_deque.pop(nums[i-k+1])
        return res
# @lc code=end

