class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return
        
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            
            cur_node.next = new_node
            new_node.next  = self.head
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            if cur_node.next == self.head:
                print(cur_node.data)
                break
            print(cur_node.data)
            cur_node = cur_node.next

llist1 = LinkedList()

llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)  

llist1.print_list()