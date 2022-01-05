#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        flagA = False
        flagB = False
        curA = headA
        curB = headB
        while curA or curB:
            if curA == curB:
                return curA
            else:
                if (not curA.next and flagA == False) :
                    curA = headB
                    flagA = True
                else:
                    curA = curA.next
                
                if (not curB.next and flagB == False):
                    curB = headA
                    flagB = True
                else:
                    curB = curB.next
        return None
                
            
        
# @lc code=end

