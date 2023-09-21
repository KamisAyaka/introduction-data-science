class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self,data):
        if not self.head:
            print("error")
            return
        current = self.head
        while current.data != data and current.next is not None:
                current=current.next
        if current.data == data:print("yes")
        else:print("error")
        return
    def delete(self,data):
        if not self.head:
            print("error")
            return
        current = self.head
        if current.data == data and current.next is not None:
            self.head = current.next
            return
        while current.next is not None:
            if current.next.data != data:
                current = current.next
        if current.next.data == data and current.next.next is not None:
            current.next = current.next.next
        elif current.next.next is None:
            current = None
        else:
            print("error")
        return
    def change(self,data1,data2):
        if not self.head:
            print("error")
            return
        current = self.head
        while current.data != data1 and current.next is not None:
            current = current.next
        if current.data == data1:
            current.data = data2
        else:
            print("error")
        return
    # 创建一个空链表
my_list = LinkedList()

# 向链表添加元素
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.search(2)
my_list.change(3,4)
my_list.delete(1)
curr = my_list.head
while curr :
    print(curr.data)
    curr=curr.next