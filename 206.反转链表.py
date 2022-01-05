#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    # 双指针法
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
    '''

    # 递归法
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(None, head)
    
    def reverse(self, node1, node2):
        if not node2:
            return node1
        next = node2.next
        node2.next = node1
        return self.reverse(node2, next) 



# @lc code=end

