"""
单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
push(value) 链表头部添加元素
append(value) 链表尾部添加元素
insert(pos, value) 指定位置添加元素
remove(item) 删除节点
search(value) 查找节点是否存在
"""


# 创建节点类
class SingleNode(object):
    """ 单链表的节点类 """
    def __init__(self, value):
        # _value存放数据元素
        self.value = value
        # _next是下一个节点的标识
        self.next = None


# 单链表实现
class SingleLinkList(object):
    """ 单链表 """

    def __init__(self):
        """ 节点 """
        self._head = None

    def is_empty(self):
        """ 判断链表是否为空 """
        return self._head == None

    def length(self):
        """ 单链表长度 """
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """ 遍历整个链表 """
        cur = self._head
        while cur != None:
            print(cur.value)
            cur = cur.next

    def push(self, value):
        """ 入栈：链表头部添加节点 """
        node = SingleNode(value)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, value):
        """ 链表尾部添加节点 """
        # 创建节点
        node = SingleNode(value)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 链表不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                # 一直找到尾部节点
                cur = cur.next
            # 尾部节点指针域指向新节点
            cur.next = node

    def insert(self, pos, value):
        """ 指定位置插入节点 """
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.push(value)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(value)
        # 找到指定位置
        else:
            node = SingleNode(value)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, value):
        """ 删除节点 """
        # 初始节点和前驱节点
        cur = self._head
        pre = None
        if cur is None:
            return
        while cur != None:
            # 找到了指定元素
            if cur.value == value:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                    cur.next = None
            else:
                # 删除的节点不是第一个节点，节点继续向后移动
                pre = cur
                cur = cur.next

    def search(self, value):
        """ 查找节点是否存在 """
        cur = self._head
        while cur != None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def pop(self):
        """ 出栈：删除并返回头部元素 """
        # 初始化当前节点
        cur = self._head
        head_val = None
        if cur is not None:
            head_val = cur.value    # 记录出栈节点的元素值
            self._head = cur.next   # 将头节点指向 出栈节点的下一个节点
            cur = None  # 将出栈节点置空
        return head_val


if __name__ == '__main__':
    link_list = SingleLinkList()
    link_list.push('sss')
    link_list.push('ddd')
    link_list.push('ff')
    link_list.push(32)
    link_list.push('oojm')
    link_list.append('mm')
    link_list.append('njn')
    link_list.append('scc')
    link_list.travel()
    print('-------------')

    p1 = link_list.pop()
    print('...p1:', p1)
    link_list.travel()

    p2 = link_list.pop()
    print('...p2:', p2)
    link_list.travel()
