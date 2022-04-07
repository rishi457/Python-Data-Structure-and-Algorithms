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
    
    def removeDuplicates(self):
        records = {}
        cur_node = self.head
        prev = None
        while cur_node:
            if cur_node.data not in records:
                records[cur_node.data] = 1
                prev = cur_node

            else:
                records[cur_node.data] += 1
                prev.next = cur_node.next 
                cur_node = None
            cur_node = prev.next

    def isPalindrome(self):
        cur_node = self.head
        testString = []
        
        while cur_node:
            testString.append(cur_node.data) 
            cur_node = cur_node.next
            
        return testString == testString[::-1]
    
    def rotate(self,val):
        cur_node = self.head
        prev = None
        end = None
        while cur_node and cur_node.data != val:
            prev = cur_node
            end = cur_node
            cur_node = cur_node.next
        prev = cur_node
        
        while cur_node:
            end = cur_node
            cur_node = cur_node.next
        
        end.next = self.head
        self.head = prev.next
        prev.next = None
        
        
        
        


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
llist1.append(10)
llist1.append(9)
llist1.append(7)
llist1.append(5)
llist1.append(3)
llist1.append(1)

#llist1.removeDuplicates()

#print(llist1.isPalindrome())
llist1.rotate(3)

llist1.print_list()