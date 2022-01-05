#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # 为None或list
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        que = [root]
        while que:
            num = len(que)
            sub_res = []
            for _ in range(num):
                node = que.pop(0)
                sub_res.append(node.val)
                if node.children:
                    que.extend(node.children)
            res.append(sub_res)
        return res
# @lc code=end

