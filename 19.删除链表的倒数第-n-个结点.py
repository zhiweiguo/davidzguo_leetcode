#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_head = ListNode(0)
        pre_head.next = head
        slow = pre_head
        fast = pre_head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return pre_head.next

# @lc code=end

