#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # 递归法
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     res = 0
    #     if not root:
    #         return res
        
    #     def traversal(root):
    #         if not root:
    #             return True
    #         left = traversal(root.left)
    #         right = traversal(root.right)
    #         if root.left and (not root.left.left) and (not root.left.right):
    #             res += root.left.val
        
    #     traversal(root)
    #     return sum(res)

    # 迭代法
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        que = [root]
        while que:
            node = que.pop(0)
            if node.left and (not node.left.left) and (not node.left.right):
                res += node.left.val
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return res
          

        
# @lc code=end

