class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get_length(self):
        if self.head == None:
            return 0
        count = 0
        itr = self.head
        while itr != None:
            count += 1
            itr = itr.next
        return count
    
    def get(self, index: int) -> int:
        count = 0
        itr = self.head
        while itr != None:
            if index == count:
                return itr.data
            itr = itr.next
            count = count + 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        temp = Node(val, self.head,prev = None)
        if self.head == None:
            self.head = temp
            return
        self.head.prev = temp
        self.head = temp
        

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None, None)
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        temp = Node(val,None,itr)
        itr.next = temp
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.get_length():
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == int(self.get_length()):
            self.addAtTail(val)
            return
        itr = self.head
        count = 0
        while itr != None:
            if count == index - 1:
                temp = Node(val,itr.next,itr)
                itr.next = temp
                temp.prev = itr
                temp.next.prev = temp
            itr = itr.next
            count = count + 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.get_length():
            return
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            #self.head.prev = None   
            return
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                if itr.next.next == None:
                    itr.next = None
                    break
                itr.next.next.prev = itr
                itr.next = itr.next.next
                break  
            itr = itr.next
            count += 1