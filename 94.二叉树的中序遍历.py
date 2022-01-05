#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         self.traversal(root, res)        
#         return res

#     def traversal(self, root, res):
#         if not root:
#             return
#         self.traversal(root.left, res)
#         res.append(root.val)
#         self.traversal(root.right, res)
#         return

class Solution:
    # 迭代法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while cur or stack:
            # 遍历左子树节点，直至到叶子节点
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right
        return res

            
# @lc code=end




def kth(nums, k):
    l = len(nums)
    if k > l:
        return []
    
    def findk(nums, left, right, k):
        pivot = partion(nums, left, right)
        if pivot == k-1:
            return  nums[:pivot+1]
        elif pivot > k-1:
            findk(nums, left, pivot, k)
        else:
            findk(nums, pivot+1, right, k)
        
    def partion(nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] > pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    return findk(nums, 0, len(nums)-1, k)
   






# -*- coding:utf-8 -*-

class Finder:
    def findKth(self, a, n, K):
        # write code here
        def findk(a, start, end, k):
            if start > end:
                return -1
            pivot = partion(a, start, end)
            if pivot == k-1:
                return a[pivot]
            elif pivot < k-1:
                return findk(a, pivot+1, end, k)
            else:
                return findk(a, start, pivot-1, k)
           
        def partion(a, left, right):
            pivot = a[left]
            while left < right:
                while left < right and a[right] <= pivot:
                    right -= 1
                a[left] = a[right]
                while left < right and a[left] >= pivot:
                    left += 1
                a[right] = a[left]
            a[left] = pivot
            return left
        
        return findk(a, 0, n-1, K)
            
