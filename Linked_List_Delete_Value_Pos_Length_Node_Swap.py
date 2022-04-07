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
    
    def delete_by_value(self,key1):
        cur_node = self.head
        prev = None
        while cur_node and cur_node.data != key1:
            prev = cur_node
            cur_node = cur_node.next
        
        if prev == None:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev.next = cur_node.next
        cur_node = None
    
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

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

length_before = llist1.length()
print("The length before deletion is", length_before)

llist1.delete_by_value(1)

length_after = llist1.length()
print("The length after deletion of a node is", length_after)


llist1.print_list()