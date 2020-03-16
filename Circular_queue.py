# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:44:48 2019

@author: Alankrit Agarwal
"""

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k=k
        self.arr=[None]*k
        self.front=0
        self.rear=-1
        self.n=0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        else:
            self.rear=(self.rear+1)%self.k
            self.arr[self.rear]=value
            
            self.n+=1
            return True
            
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():return False
        else:
            self.arr[self.front]=None
            self.n-=1
            self.front=(self.front+1)%self.k
            return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:return self.arr[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:return self.arr[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.n==0
        
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.n==self.k
    
    def print_queue_details(self):
        print(self.arr,self.front,self.rear,self.n,sep=' ')
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
print(obj.enQueue(6))
print(obj.Rear())
print(obj.Rear())
obj.print_queue_details()
print(obj.deQueue())
print(obj.enQueue(5))
print(obj.Rear())
print(obj.deQueue())
print(obj.Front())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
#obj.print_queue_details()
#obj.enQueue(3)
#obj.enQueue(4)
#obj.print_queue_details()

#obj.print_queue_details()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()