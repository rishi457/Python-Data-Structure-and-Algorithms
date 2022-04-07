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
        cur_node = self.head
        prev = None

        while cur_node:
          nxt = cur_node.next
          cur_node.next = prev
          prev = cur_node 
          cur_node = nxt  
        self.head = prev
    
    def mergelist(self, list2):
        p = self.head
        q = list2.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head= s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if p is None:
            s.next = q
        if q is None:
            s.next = p
        
        self.head = new_head

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
llist2 = Linkedlist()
llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(7)
llist1.append(9)

llist2.append(2)
llist2.append(4)
llist2.append(6)
llist2.append(8)
llist2.append(10)

#llist1.node_swap(3,9)
llist1.mergelist(llist2)
llist1.reverse()
llist1.print_list()