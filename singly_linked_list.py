from typing import Optional


class Node():
    """Node of singly linked list."""
    def __init__(self, data: int, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class SinglyLinkedList():
    def __init__(self):
        self.__head = None

    def insert_to_head(self, value: int):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def insert_after(self, node: Node, value: int):
        if node is None:  # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node: Node, value: int):
        if node is None or self.__head is None:
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pos = self.__head
        found = False
        while pos.next:
            if pos.next == node:
                found = True
                break
            else:
                pos = pos.next

        if found:
            pos.next = new_node
            new_node.next = node

    def find_by_value(self, value: int):
        if self.__head is None:
            return

        pos = self.__head
        found = False
        while pos:
            if value == pos.data:
                found = True
                break
            else:
                pos = pos.next

        if found:
            return pos
        else:
            return None

    def find_by_index(self, index: int):
        if index < 0:
            return None

        pos = self.__head
        i = 0
        while i < index:
            if pos.next:
                i += 1
                pos = pos.next
            else:
                return None

        return pos

    def print_all(self):
        pos = self.__head
        if (pos is None):
            print('no data in list')
            return

        while pos.next:
            print(str(pos.data) + ' --> ', end='')
            pos = pos.next
        print(str(pos.data))

    def delete_by_node(self, node: Node):
        if node is None or self.__head is None:
            return

        if node == self.__head:
            self.__head = node.next
            return

        pos = self.__head
        found = False
        while pos.next:
            if pos.next == node:
                found = True
                break
            else:
                pos = pos.next

        if found:
            pos.next = node.next

    def delete_by_value(self, value: int):
        if self.__head is None:
            return

        if self.__head.data == value:
            self.__head = self.__head.next
            return

        pos = self.__head
        found = False
        while pos.next:
            if value == pos.next.data:
                found = True
                break
            else:
                pos = pos.next

        if found:
            pos.next = pos.next.next

    def delete_last_N_node(self, n: int):
        if self.__head is None:
            return

        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next
            if fast is None:
                return
            else:
                step += 1

        if fast.next is None:
            self.__head = self.__head.next
            return

        while fast.next is not None:
            temp = slow
            fast = fast.next
            slow = slow.next
        else:
            temp.next = slow.next

    def find_mid_node(self):
        if self.__head is None:
            return

        fast = self.__head
        slow = self.__head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reversed_self(self):
        '''翻转链表自身.'''
        if self.__head is None or self.__head.next is None:  # 如果链表为空，或者链表只有一个节点
            return

        pre = self.__head
        node = self.__head.next
        while node is not None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self.__head.next = None
        self.__head = pre

    def __reversed_with_two_node(self, pre: Node, node: Node):
        '''翻转相邻两个节点.
        参数:
            pre:前一个节点
            node:当前节点
        返回:
            (pre,node):下一个相邻节点的元组
        '''
        tmp = node.next
        node.next = pre
        pre = node  # 这样写有点啰嗦，但是能让人更能看明白
        node = tmp
        return (pre, node)

    def convert_array_to_list(self, arr):
        for value in arr:
            self.insert_to_head(value)
        self.reversed_self()

    def convert_to_array(self):
        if self.__head is None:
            return []

        arr = []
        pos = self.__head
        while pos:
            arr.append(pos.data)
            pos = pos.next

        return arr


# if __name__ == "__main__":
#     l = SinglyLinkedList()
#     for value in range(0, 11):
#         l.insert_to_head(value)
#     l.print_all()

#     l.reversed_self()
#     l.print_all()

#     node = l.find_mid_node()
#     print(node.data)

#     node = l.find_by_index(0)
#     print(node.data)

#     node = l.find_by_value(8)
#     print(node.data)

#     l.delete_by_node(node)
#     l.print_all()

#     l.delete_by_value(5)
#     l.print_all()
