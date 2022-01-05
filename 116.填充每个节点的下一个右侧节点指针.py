#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        que = [root]
        while que:
            num = len(que)
            for i in range(num):
                node = que.pop(0)
                if i == num-1:
                    node.next = None
                else:
                    node.next = que[0]
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        return root

        
# @lc code=end

