class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.next = new_node.next
            self.prev = new_node.prev
            return
        else:
            cur_node = self.head
            new_node = Node(data)
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    
    def prepend(self,data):
        if self.head is None:
            print("Print Double Link list is non-existent")
            return
        
        else:
            new_node = Node(data)
            cur_node = self.head

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
            
            
    def print_list(self):
        
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

llist1 = DoubleLinkedList()

llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)
llist1.prepend(9)
llist1.prepend(7)
llist1.prepend(5)
llist1.prepend(3)
llist1.prepend(1)



llist1.print_list()



    