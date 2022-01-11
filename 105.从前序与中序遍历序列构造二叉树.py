#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        l = len(preorder)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(preorder[0])
        return self.traversal(preorder, inorder, 0, l-1, 0, l-1)
         
    def traversal(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        mid_val = preorder[pre_start]
        mid_node = TreeNode(mid_val)
        if pre_start == pre_end:
            return mid_node
        mid_idx = 0
        for i in range(in_start, in_end+1):
            if inorder[i] == mid_val:
                mid_idx = i
        left_num = mid_idx - in_start
        mid_node.left = self.traversal(preorder, inorder, pre_start+1, pre_start+left_num, in_start, mid_idx-1)
        mid_node.right = self.traversal(preorder, inorder, pre_start+left_num+1, pre_end, mid_idx+1, in_end)
        return mid_node

# @lc code=end

