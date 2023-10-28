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
    def oddEvenList(self , head ):
        # write code here
        if head is None or head.next is None:
            return head

        root = ListNode(-1)
        root.next = head

        even = head.next
        odd = head
        even_root = even
        while 1:
            odd_nxt = even.next
            odd.next = odd_nxt
            if odd_nxt is None:
                break
            odd = odd_nxt
            if odd_nxt:
                even_nxt = odd_nxt.next
                even.next = even_nxt
                even = even_nxt
                if even is None:
                    break
            else:
                break

        odd.next = even_root
        return root.next

if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node4 = ListNode(4)
    # node3.next = node4
    node2.next = node3
    node1.next = node2

    solution.oddEvenList(node1)