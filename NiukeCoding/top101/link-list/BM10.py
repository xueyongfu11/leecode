# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        node1 = pHead1
        node2 = pHead2

        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = pHead2

            if node2:
                node2 = node2.next
            else:
                node2 = pHead1

        if node1:
            return node1
        else:
            return None
