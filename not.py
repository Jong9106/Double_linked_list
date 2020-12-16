#!/usr/bin/python3
# Create the Node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Create the doubly linked list
class doubly_linked_list:
   def __init__(self):
      self.head = None
      self.tail = None

# Define the push method to add elements
   def insert_head(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

   def insert_end(self, NewVal):
      if self.head is None:
         NewNode = Node(NewVal)
         NewNode.next = None
         self.head = NewNode
         return
      n = self.head
      #elif self.head.next == None:
      #self.head.next = NewNode
      # NewNode.prev = self.head
      # NewNode.next = None
      while n.next is not None:
         n = n.next
      NewNode = Node(NewVal)
      n.next = NewNode
      NewNode.next = None
   # Define the insert method to insert the element
   def insert_head2(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
            NewNode.next.prev = NewNode

# Define the method to print the linked list
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

# Traversing a Doubly linked list
   def traverse_list(self):
      if self.head is None:
         print("List has no element")
         return
      else:
         n = self.head
      a = 0
      while n is not None:
         a += 1         
         n = n.next
      print("List have -> {:d} elements".format(a))

   # Deleting Elements from the End
   def delete_at_end(self):
      if self.head is None:
         print("The list has no element to delete")
         return
      if self.head.next is None:
         self.head = None
         return
      n = self.head
      while n.next is not None:
         n = n.next
         n.next = None

   def deleteFromStart(self):    
      #Checks whether list is empty    
      if(self.head == None):    
         return;    
      else:    
         #Checks whether the list contains only one element    
         if(self.head != self.tail):    
            #head will point to next node in the list    
            self.head = self.head.next;    
            #Previous node to current head will be made None    
            self.head.previous = None;    
                    
            #If the list contains only one element     
            #then, it will remove the node, and now both head and tail will point to None    
    
         else:    
            self.head = self.tail = None;    


dllist = doubly_linked_list()
dllist.insert_head(12)
dllist.insert_end(8)
dllist.insert_head(62)
dllist.insert_end(7)
dllist.insert_head(16)
dllist.listprint(dllist.head)
print()
dllist.deleteFromStart()
dllist.listprint(dllist.head)
print()
dllist.deleteFromStart()
dllist.listprint(dllist.head)
      
print()
dllist.traverse_list()
