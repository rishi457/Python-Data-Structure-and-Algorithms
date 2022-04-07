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

    def reverse(self):
        pass
    
    def mergelist(self, list2):
        pass

    def node_swap(self, val1, val2):
        cur_node1 = self.head
        cur_node2 = self.head

        prev1 = None
        prev2 = None

        if val1 == val2:
            return
        
        while cur_node1 and cur_node1.data != val1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next
        
        while cur_node2 and cur_node2.data != val2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        
        if prev1:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        
        if prev2:
            prev2.next = cur_node1
        else:
            self.head = cur_node1
        
        cur_node1.next, cur_node2.next = cur_node2.next,cur_node1.next

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next        

llist1 = Linkedlist()

llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(7)
llist1.append(9)

llist1.node_swap(3,9)
llist1.print_list()