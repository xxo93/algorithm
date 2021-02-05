"""
单向循环链表的操作:
is_empty() 判断链表是否为空
length() 返回链表的长度
travel() 遍历
add(value) 在头部添加一个节点
append(value) 在尾部添加一个节点
insert(pos, value) 在指定位置pos添加节点
remove(value) 删除一个节点
search(value) 查找节点是否存在
"""
# from PyVbord.apps.AAAtest.APy.链表.common import get_linked_list, read_linked_list, ListNode


# 创建节点类
class Node(object):
    """节点"""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinCycLinkedList(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """ 判断链表是否为空 """
        return self._head is None

    def length(self):
        """ 返回链表的长度 """
        if self.is_empty():
            return 0

        cur = self._head
        count = 1
        while cur.next != self._head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """ 遍历 """
        if self.is_empty():
            return
        # 首次头节点
        linked_list = [self._head.value]

        cur = self._head
        while cur.next != self._head:
            linked_list.append(cur.value)
            cur = cur.next

        # 循环一遍之后的头节点
        linked_list.append(cur.value)

        return '->'.join(linked_list)

    def add(self, value):
        """ 在头部添加一个节点 """
        node = Node(value)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加的节点指向 _head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将最后的节点指向新的node
            cur.next = node
        return node

    def append(self, value):
        """ 在尾部添加一个节点 """
        node = Node(value)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表的尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head
            
    def insert(self, pos, value):
        """ 在指定位置pos>0添加节点value """
        node = Node(value)
        # 记录链表长度
        length = self.length()
        if pos <= 0:
            self.add(value)
            return value
        if pos > length-1:
            self.append(value)
            return value
        # 移动到指定位置的前一个节点
        cur = self._head
        count = 0
        while count < pos-1:
            cur = cur.next

        node.next = cur.next
        cur.next = cur

        return value

    def remove(self, value):
        """ 删除一个节点 """

    def remove_pos(self, value):
        """ 删除指定节点 """

    def search(self, value):
        """ 查找节点是否存在 """
        pass


if __name__ == '__main__':
    ll = SinCycLinkedList()


