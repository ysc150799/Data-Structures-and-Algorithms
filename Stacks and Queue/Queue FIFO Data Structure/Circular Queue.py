class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.head == -1 and self.tail == -1:
                self.head = 0
                self.tail = 0
                self.queue[self.tail] = value
                return True
            else:
                self.tail = (self.tail+1) % self.k 
                self.queue[self.tail] = value
                return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():            
            if self.head == self.tail:
                self.head, self.tail = -1, -1
                self.queue = [None] * self.k
                return True
            else:
                self.queue[self.head] = None
                self.head = (self.head+1) % self.k 
                return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.k == self.head:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()