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

    def removebyval(self,val):
        cur_node = self.head
        prev = None
        
        if self.head.data == val:
            if self.head.data == self.head:
                self.head = None
            else:
                while cur_node.next != self.head:
                    cur_node = cur_node.next
                cur_node.next = self.head.next
                self.head = self.head.next

        else:
            while cur_node.next != self.head and cur_node.data != val:
                prev = cur_node
                cur_node = cur_node.next
            prev.next = cur_node.next
            cur_node = None

    def split_linked_list(self,val):
        cur = self.head
        prev = None

        while cur.next != self.head and cur.data != val:
            prev = cur
            cur = cur.next
        prev = cur
        
        second_split = LinkedList()
        new_pointer = second_split.head
        
        
        while cur.next.data != self.head.data:
            second_split.append(cur.next.data)
            cur = cur.next
            
        prev.next = self.head
        cur.next = new_pointer
            
        self.print_list()
        print("Second Split")
        second_split.print_list()

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
llist1.append(11)
#llist1.removebyval(11)
llist1.split_linked_list(3)
#llist1.print_list()