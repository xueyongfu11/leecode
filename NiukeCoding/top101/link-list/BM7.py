# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = pHead
        slow = pHead

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        fast = pHead  # 一个从头开始，一个从交会点开始，再次相交就是入口点
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
