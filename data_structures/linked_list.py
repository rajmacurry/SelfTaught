class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self,data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
        
    def print_node(self):
        print(self.data)
            
the_list = LinkedList()
the_list.append_node("Monday")
the_list.append_node(("Tuesday"))

the_list.print_list()
