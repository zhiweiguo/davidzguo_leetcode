#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        l = len(inorder)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(inorder[0])
        return self.traversal(inorder, postorder, 0, l-1, 0, l-1)
    
    # 左闭右闭区间, inorder[in_start, in_end], postorder[post_start, post_end]
    def traversal(self, inorder, postorder, in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return None
        mid_val = postorder[post_end]
        mid_node = TreeNode(mid_val)
        if post_start == post_end:  # 区间长度为1时，说明为叶子节点，直接返回
            return mid_node
        mid_idx = 0
        for i in range(in_start, in_end+1):
            if inorder[i] == mid_val:   # 中序遍历的根节点索引
                mid_idx = i
        left_num = mid_idx - in_start
        mid_node.left = self.traversal(inorder, postorder, in_start, mid_idx-1, post_start, post_start+left_num-1)
        mid_node.right = self.traversal(inorder, postorder, mid_idx+1, in_end, post_start+left_num, post_end-1)
        return mid_node



# @lc code=end

