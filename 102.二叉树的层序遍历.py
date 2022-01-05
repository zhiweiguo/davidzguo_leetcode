#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     res = []
    #     nodes = [root]
    #     while len(nodes) > 0:
    #         nums = len(nodes)
    #         tmp = []
    #         for _ in range(nums):
    #             node = nodes.pop(0)
    #             tmp.append(node.val)
    #             if node.left:
    #                 nodes.append(node.left)
    #             if node.right:
    #                 nodes.append(node.right)
    #         res.append(tmp)
    #     return res

    # 二刷
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = [root]
        while que:
            num = len(que)
            sub_res = []
            for _ in range(num):
                node = que.pop(0)
                sub_res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(sub_res)
        return res



# @lc code=end

