#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 递归法
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next_next = head.next.next
        new_head =head.next
        new_head.next = head
        head.next = self.swapPairs(next_next)
        return new_head


    # # 迭代法
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     pre_head = ListNode(0)
    #     pre_head.next = head
    #     cur = pre_head
    #     while cur.next and cur.next.next:
    #         cur_next = cur.next
    #         cur_next_next_next = cur.next.next.next

    #         cur.next = cur_next.next
    #         cur.next.next = cur_next
    #         cur.next.next.next = cur_next_next_next
            
    #         cur = cur.next.next

    #     return pre_head.next

# @lc code=end

