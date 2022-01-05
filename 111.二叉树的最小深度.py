#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left * right == 0:            # 当有一个节点为空时，需要使用不为空的节点深度
            return max(left, right) + 1
        else:                            # 两节点都不为空时，使用较小的节点深度
            return min(left, right) + 1  



# @lc code=end

