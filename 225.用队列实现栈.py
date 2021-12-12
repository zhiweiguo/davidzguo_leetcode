#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        self.my_deque = deque()

    def push(self, x: int) -> None:
        self.my_deque.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        # 只用一个队列实现
        # 将队列中原来的元素依次弹出，只留最后一个元素
        # 弹出的元素再重新入队列
        # 最后将第一个元素弹出即可
        num = len(self.my_deque)-1
        for i in range(num):
            self.my_deque.append(self.my_deque.popleft())
        return self.my_deque.popleft()

    def top(self) -> int:
        tmp = self.pop()
        self.push(tmp)
        return tmp

    def empty(self) -> bool:
        return len(self.my_deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

