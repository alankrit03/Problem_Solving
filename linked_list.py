# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:24:17 2019

@author: Alankrit Agarwal
"""

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
# =============================================================================
# Declaring the linked list class 
# =============================================================================
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

 
    def insert(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

 
    def display(self):
        current = self.head
        while current.next is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print(current.data)
 
linklist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    linklist.insert(data)
print('The linked list: ', end = '')
linklist.display()