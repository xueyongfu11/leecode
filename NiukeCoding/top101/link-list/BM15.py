#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head):
        # write code here
        if head is None or head.next is None:
            return head

        root = ListNode(-1)
        root.next = head
        while head:
            val = head.val
            cur = head.next
            while cur:
                next_val = cur.val
                if next_val == val:
                    cur = cur.next
                else:
                    break
            head.next = cur
            head = cur
        return root.next

