class PyLinkedList:
# ###########################
# Class Variables
   head = Node("")

# ###########################
# Public Methods   
   def add(self, key):
      body = Node(key)
      body.next = head
      head = body
      return
   
   def remove(self, key):
      temp = head
      while temp.key

class Node(PyLinkedList):
   # ###########################
   # Constructor
   def __init__ (self, key):
      self.key = key
      self.next = null
