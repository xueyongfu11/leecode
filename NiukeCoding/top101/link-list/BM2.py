class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类

class Solution1:
    '''
    记录反转链表反转之后的头尾添加到原始链表中
    存在bug
    '''

    def reverseBetween(self, head, m: int, n: int):
        # write code here

        node = ListNode(-1)
        node.next = head

        i = 1  # 从第二个node开始
        cur_node = head
        pre_li_tail_node = None  # 保存pre_li的尾node
        reverse_li_head_node = None  # 反转好的链表的头节点
        while cur_node:
            if i == m - 1:
                # 将pre_li的尾节点保存下来
                pre_li_tail_node = cur_node
                cur_node = cur_node.next
            elif i == m == n:
                cur_node = cur_node.next
            elif i == m:
                tmp_node = cur_node.next
                cur_node.next = None
                reverse_li_head_node = cur_node

                cur_node = tmp_node
            elif i == n:
                tmp_node = cur_node.next
                cur_node.next = reverse_li_head_node
                reverse_li_head_node = cur_node

                # 将反转链表的头连接起来
                if pre_li_tail_node:
                    pre_li_tail_node.next = reverse_li_head_node

                    # 找到反转链表的尾
                    while pre_li_tail_node.next:
                        pre_li_tail_node = pre_li_tail_node.next
                    # 将反转链表的尾和剩余链表链接起来
                    pre_li_tail_node.next = tmp_node
            elif m < i and i < n:
                tmp_node = cur_node.next
                cur_node.next = reverse_li_head_node
                reverse_li_head_node = cur_node
                cur_node = tmp_node
            else:
                cur_node = cur_node.next
            i += 1
        return node.next


class Solution:
    def reverseBetween(self, head, m: int, n: int):
        # 首先定义一个新的头结点
        result = ListNode(-1)
        result.next = head
        pre = result
        # 遍历到m-1个结点
        for i in range(m - 1):
            pre = pre.next
        # 此时pre指向m-1结点,pre.next指向m结点
        # 定义当前要反转的结点与前一结点
        temp = None
        cur = pre.next
        # 进行区间链表反转
        for i in range(m, n + 1):
            back = cur.next
            cur.next = temp
            temp = cur
            cur = back
        # 循环完之后，temp指向n结点，cur指向n+1结点
        # m结点下一个是n+1结点，m-1结点下一个是n结点
        # pre.next任然指向第m个结点，而第m个结点在之前的操作中已经变成了反转链表中的尾节点，并指向了空
        # 相当于有两个指针指向了第m个结点
        # 此时希望第m个节点指向反转区间之后的链表，并且第m-1个节点指向已经反转链表的头节点
        pre.next.next = cur
        pre.next = temp
        return result.next


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next =node5
    node3.next = node4
    node2.next = node3
    node1.next = node2

    solution.reverseBetween(node1, 2, 4)
