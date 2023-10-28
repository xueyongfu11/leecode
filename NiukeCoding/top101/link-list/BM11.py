# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self, head1, head2):
        # write code here
        pre1 = None
        cur1 = head1
        while cur1:
            nxt = cur1.next
            cur1.next = pre1
            pre1 = cur1
            cur1 = nxt

        pre2 = None
        cur2 = head2
        while cur2:
            nxt = cur2.next
            cur2.next = pre2
            pre2 = cur2
            cur2 = nxt

        mod = 0
        root = ListNode(-1)
        nhead = root
        while pre1 or pre2:
            val = mod
            if pre1:
                val += pre1.val
                pre1 = pre1.next

            if pre2:
                val += pre2.val
                pre2 = pre2.next

            mod = val // 10
            nhead.next = ListNode(val % 10)
            nhead = nhead.next

        if mod != 0:
            nhead.next = ListNode(mod)

        # 最后载反转
        pre = None
        cur = root.next
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
