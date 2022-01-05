#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.traversal(root, res)
#         return res
    
#     def traversal(self, root, res):
#         if not root:
#             return
#         res.append(root.val)
#         self.traversal(root.left, res)
#         self.traversal(root.right, res)

class Solution:
    # 迭代法
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]    # 根节点入栈
        while len(stack) > 0:
            node = stack.pop()   # 弹出最后一个元素
            res.append(node.val)
            if node.right:       # 前序遍历是中左右，所以要先将右节点入栈
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# @lc code=end

