from PyVbord.apps.AAAtest.APy.链表.common import get_linked_list, read_linked_list, ListNode


class Solution:
    def __init__(self):
        self.successor = None

    def reverse_recursive(self, head: ListNode) -> ListNode:
        """ 递归法
        反转单链表
        :param head: 反转前的头节点
        :return: 反转后的头节点
        """
        # 记录返回最后一个节点
        if not head or not head.next:
            return head

        # 逐层递归返回最后一个节点(last_Node 即 new head)，head为倒数第二个节点
        last_Node = self.reverse_recursive(head.next)

        # 保存反转完成的子链表
        t_head = head.next
        # 确定反转完成的子链表的下一个节点指向
        t_head.next = head
        head.next = None

        return last_Node

    def reverse_N_recursive(self, head: ListNode, n: int) -> ListNode:
        """ 递归法
        反转链表的前 n 个节点
        :param head: 反转前的头节点
        :return: 反转后的头节点
        """
        if n == 1:
            # 记录第n+1个节点
            self.successor = head.next
            return head

        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last_node = self.reverse_N_recursive(head.next, n - 1)

        head.next.next = head

        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor

        return last_node

    # 单链表就地反转
    def reverse_iter(self, head: ListNode) -> ListNode:
        """ 迭代法
        就地反转单链表
        :param head: 反转前的头节点
        :return: 反转后的头节点
        """
        if head == None:
            return head

        preNode = None

        while head is not None:
            nextNode = head.next  # 1 保存下一个节点
            head.next = preNode  # 2 改变当前的节点指针域
            preNode = head  # 3 将当前节点变为下一个节点的前一个结点
            head = nextNode  # 4 将指针移向下一个节点位置

        return preNode


if __name__ == '__main__':
    s = Solution()

    head = get_linked_list([1, 2, 3, 4, 5])
    # print('Head Node:', head)

    print('Initial linked_list：', read_linked_list(head))

    # 1.递归法: 反转单链表
    # head = s.reverse_recursive(head)
    # 2.递归法: 反转链表的前n个节点
    # head = s.reverse_N(head, 3)
    # 3.迭代法: 就地反转单链表
    head = s.reverse_iter(head)

    print('Reverse linked_list：', read_linked_list(head))
