class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new node and add node to the end
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        # create node and add node to he beginning
        pass

    def insert(self, index, value):
        # create new node and add node to the specified index
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    def pop(self):
        if self.head is None:
            return "List is empty"
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            value = temp.value
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            return value


my_linked_list = LinedList(1)
print(my_linked_list.pop())
my_linked_list.print_list()
print(my_linked_list.pop())
