#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#


# @lc code=start

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pre_head = Node(0)
        self.count = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index and index < self.count:
            node = self.pre_head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            index = 0
        if index > self.count:
            return
        self.count += 1
        add_node = Node(val)
        pre = self.pre_head
        cur = pre.next
        for _ in range(index):
            pre, cur = cur, cur.next
        pre.next = add_node
        add_node.next = cur

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.count:
            self.count -= 1
            pre = self.pre_head
            for _ in range(index):
                pre = pre.next
            pre.next = pre.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

