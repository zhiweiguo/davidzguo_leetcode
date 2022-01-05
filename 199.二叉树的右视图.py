#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(sub_res[-1])   # 层序遍历之后只把该层最后一个元素放入最后结果中

        return res


# @lc code=end

