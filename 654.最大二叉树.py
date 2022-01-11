#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.traversal(nums)
        
    def traversal(self, nums):
        root = TreeNode()
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            root.val = nums[0]
            return root
        max_val = 0
        max_idx = 0
        for i in range(l):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
        root.val = max_val
        if max_idx > 0:
            root.left = self.traversal(nums[:max_idx])
        if max_idx < l-1:
            root.right = self.traversal(nums[max_idx+1:])
        return root




# @lc code=end

