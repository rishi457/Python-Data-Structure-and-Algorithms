class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        cur_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = cur_node
            self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

llist1 = Linkedlist()

llist1.prepend(3)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.prepend(1)


llist1.print_list()
