class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linklist(node_list: list) -> ListNode:
    """ 给定列表，生成链表 """
    if len(node_list) == 0:
        return ListNode()
    header = ListNode(node_list[0])
    p = header
    for node_val in node_list[1:]:
        nxt = ListNode(node_val)
        p.next = nxt
        p = p.next
    return header


def linklist_to_list(header: ListNode) -> list:
    """ 给定链表，生成列表 """
    node_val_list = []
    p = header
    while p:
        node_val_list.append(p.val)
        p = p.next
    return node_val_list


def get_linked_list(v_lis: list) -> ListNode:
    """ 数组转链表 """
    lk_list = []
    for v in v_lis:
        lk_list.append(ListNode(v))

    for idx, node in enumerate(lk_list):
        if idx == len(lk_list) - 1:
            break
        node.next = lk_list[idx + 1]
    return lk_list[0] if len(lk_list) != 0 else None


def read_linked_list(head: ListNode) -> str:
    """ 输出链表每个节点元素 """
    temp = []
    cur = head
    while cur:
        temp.append(str(cur.val))
        cur = cur.next
    # print("->".join(temp))
    return "->".join(temp)
