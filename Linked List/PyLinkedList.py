class PyLinkedList:
# ###########################
# Class Variables
   head = Node("")
   int count = 0;

# ###########################
# Public Methods   
   def add(self, key):
      body = Node(key)
      body.next = head
      head = body
      count++
      return
   
   def remove(self, str):
      temp = head
      while !(temp.key == "" && temp.next == null):
         if temp.key == str:
            temp.next = temp.next.next
            count--
         temp = temp.next
      return
   
   def hasString(self, str):
      temp = head
      while (temp.next != null):
         if temp.key == str:
            return true
         temp = temp.next
      return
   
   def isEmpty(self):
      return (count == 0)

   def getLength(self):
      return count; 
   
# ###############################
# Sub-Class
class Node(PyLinkedList):
   # ###########################
   # Constructor
   def __init__ (self, key):
      self.key = key
      self.next = null
