#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node_dict = {}
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.node_dict:
            return self.node_dict[root]
        do_it = root.val \
                + (0 if not root.left else self.rob(root.left.left)+self.rob(root.left.right)) \
                + (0 if not root.right else self.rob(root.right.left)+self.rob(root.right.right))                 
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do)
        self.node_dict[root] = res
        return res

# @lc code=end

