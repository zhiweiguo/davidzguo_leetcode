#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
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
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(max(sub_res))
        return res
# @lc code=end

