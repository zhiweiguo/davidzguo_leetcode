#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                 return (node1.val==node2.val) and helper(node1.left, node2.right) and helper(node1.right, node2.left) 
        return helper(root, root)
# @lc code=end

