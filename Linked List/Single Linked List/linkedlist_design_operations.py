class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0                            #length -> length of the linked list

    def get(self, index: int) -> int:
        '''
        get function returns the data at an index
        '''
        if index<0 or index>=self.length:
            return -1
        else:
            if index == 0:
                return self.head.data
            else:
                curr = self.head                    #curr -> current pointer
                for _ in range(index):              
                    curr = curr.next
                return curr.data
            
    def addAtHead(self, val: int) -> None:
        '''
        addAtHead function adds a node at first position
        '''
        self.length += 1                
        self.head = Node(val,self.head)
        
    def addAtTail(self, val: int) -> None:
        '''
        addAtTail function adds a node at last position
        '''
        if self.head == None:
            self.addAtHead(val)
        else:
            self.length += 1
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val,None)
        

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        addAtIndex function adds a node at index position provided in function call
        '''
        if index<0 or index>self.length:
            return -1
        else:
            if index == 0:
                self.addAtHead(val)
            else:
                self.length += 1
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = Node(val,curr.next)
                
    def deleteAtIndex(self, index: int) -> None:
        '''
        deleteAtIndex function deletes a node at index position provided in function call
        '''
        if index<0 or index>=self.length:
            return -1
        else:
            self.length -= 1
            if index == 0:
                self.head = self.head.next
            else:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)