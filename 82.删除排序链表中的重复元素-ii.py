#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_head = ListNode(0, head)
        cur = pre_head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return pre_head.next


# @lc code=end

