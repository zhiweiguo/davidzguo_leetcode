#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     # 递归法
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.traversal(root, res)
#         return res
        
#     def traversal(self, root, res):
#         if not root:
#             return
#         self.traversal(root.left, res)
#         self.traversal(root.right, res)
#         res.append(root.val)

class Solution:
    # 迭代法
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1] #类似于前序遍历，倒序输出结果


# @lc code=end

