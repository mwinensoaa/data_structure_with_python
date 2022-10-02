class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_from_front(self, data):
        new_node = Node(data)
        if self.is_empty_list():
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def add_from_back(self, data):
        if self.is_empty_list():
            self.add_from_front(Node(data))
        else:
            itr = self.head
            while itr is not None:
                if itr.next_node is None:
                    itr.next_node = Node(data)
                    return
                itr = itr.next_node

    def size(self):
        size = 0
        if self.is_empty_list():
            size = 0
        else:
            itr = self.head
            while itr is not None:
                size += 1
                itr = itr.next_node
        return size

    def print_list(self):
        if self.is_empty_list():
            print("The linkedlist is empty")
            return
        itr = self.head
        links = ''
        while itr is not None:
            links += str(itr.data) + "---->"
            itr = itr.next_node
        print(links)

    def remove_from_front(self):
        if self.is_empty_list():
            print('list is empty')
        head = self.head
        if head.next_node is not None:
            self.head = head.next_node
            head.next_node.prev_node = None

    def remove_from_back(self):
        if self.is_empty_list():
            print("List is empty..")
        else:
            itr = self.head
            while itr is not None:
                next_node = itr.next_node
                if next_node.next_node is None:
                    itr.next_node = None
                    break
                itr = itr.next_node
        pass

    def remove_after_a_given_node(self, data):
        if self.is_empty_list():
            print('The list is empty')
        elif self.head.next_node is None:
            print('There is only one element in the list')
        else:
            head_node = self.head
            while head_node is not None and head_node.next_node is not None:
                next_node = head_node.next_node
                if data == next_node.data:
                    head_node.next_node = next_node.next_node
                    next_node.pre_node = head_node
                    break
                head_node = head_node.next_node

    def is_empty_list(self) -> bool:
        return self.head is None

    def add_after_a_given_node(self, data, new_data):
        if self.is_empty_list():
            print('The list is empty')
        else:
            head_node = self.head
            while head_node is not None:
                if data == head_node.data.data:
                    new_node = Node(new_data)
                    new_node.next_node = head_node.next_node
                    head_node.next_node = new_node
                    new_node.prev_node = head_node
                    break
                head_node = head_node.next_node


if __name__ == '__main__':
    llist = LinkedList()
    llist.add_from_front(Node(20))
    llist.add_from_front(Node(10))
    llist.add_from_front(Node(22))
    print(f"the size of the list is : {llist.size()}")
    print('================after adding node from the front=======================')
    llist.print_list()
    llist.add_from_back(Node(81))
    llist.add_from_back(Node(82))
    print('================after adding from the back===================')
    llist.print_list()
    llist.add_after_a_given_node(20, 399)
    print('===============after adding after a given node=================')
    llist.print_list()
    llist.remove_from_front()
    print('=============after removing from the front=================')
    llist.print_list()
    llist.remove_from_back()
    print('=============after removing a node from the back=================')
    llist.print_list()
    llist.remove_after_a_given_node(10)
    print('=============after removing after a give node=================')
    llist.print_list()
