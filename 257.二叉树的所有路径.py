#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        path = [str(root.val)]
        que = [root]
        while que:           
            node = que.pop(0)
            cur_path = path.pop(0)
            if not (node.left or node.right):
                res.append(cur_path)
            if node.left:
                que.append(node.left)
                path.append(cur_path+'->'+str(node.left.val))
            if node.right:
                que.append(node.right)
                path.append(cur_path+'->'+str(node.right.val))
        return res




# @lc code=end

