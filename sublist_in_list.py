# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:31:38 2019

@author: Alankrit Agarwal
"""
# =============================================================================
# Declaring Node class
# =============================================================================
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
        
        
# =============================================================================
# Creating the function that checks if the list1 is present list2 or not.
# Feel free to copy code and give in your own data using the insert function,
# and play around with code.
# =============================================================================
        
def list1_in_list2():
    current1=list1.head
    current2=list2.head

    while(current1 and current2):
    
        if current2.data == current1.data :
            current1=current1.next
            current2=current2.next
        
            
# =============================================================================
# Here,below we check if the current data on list 2 is same as first node or not.
# If it is not equal then we move the pointer on list 2 one place forward
# otherwise we only move list1 pointer to head.
# So, whatever happens list1 pointer goes back to head whenever we get a situation
# where data at list1 pointer and list2 pointer are not equal.
# =============================================================================
        else:    
            if current2.data != list1.head.data:
                current2=current2.next
            
            current1=list1.head
    

    if not current1:
        print('LIST FOUND')
    else:print('LIST NOT FOUND')
        
        
        
list1=LinkedList()
list2=LinkedList()

list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)

list2.insert(1)
list2.insert(2)
list2.insert(8)
list2.insert(5)
list2.insert(2)
list2.insert(3)
list2.insert(1)
list2.insert(2)
list2.insert(3)
list2.insert(4)

print('List1:',end=' ')
list1.display()

print('List2:',end=' ')
list2.display()

list1_in_list2()