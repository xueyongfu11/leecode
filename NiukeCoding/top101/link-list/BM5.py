class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self, head, k):
        # write code here

        # 找到每组的尾节点
        tail = head
        for _ in range(k):

            if tail is None:
                return head
            # 放在if后面
            tail = tail.next

        # 反转
        pre = None
        cur = head
        while cur != tail:
            nxt = cur.next
            cur.next = pre

            # 顺序不能错
            pre = cur
            cur = nxt

        head.next = self.reverseKGroup(tail, k)
        return pre


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2

    solution.reverseKGroup(node1, 2)
