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
        pre_root = ListNode(-2)
        pre_root.next = root

        while head:
            val = head.val
            cur = head.next
            n = 0
            while cur:
                next_val = cur.val
                if next_val == val:
                    n += 1
                    cur = cur.next
                else:
                    break
            if n == 0:
                root.next = head
                root = head
            head = cur
        root.next = head
        return pre_root.next.next
