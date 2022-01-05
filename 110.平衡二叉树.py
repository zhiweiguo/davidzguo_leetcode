#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isBalance = True
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return self.isBalance
        
        def deep(root):
            if not root:
                return 0
            left = deep(root.left)
            right = deep(root.right)
            if abs(left-right)>1:
                self.isBalance = False
            return max(left,right)+1
        deep(root)
        return self.isBalance
# @lc code=end

