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
        pass

    def prepend(self, value):
        # create node and add node to he beginning
        pass

    def insert(self, index, value):
        # create new node and add node to the specified index
        pass
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_linked_list = LinedList(4)
my_linked_list.printList()
