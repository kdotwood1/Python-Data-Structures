class Stack:
# ###########################
# Class Variables
   head = Node("")

# ###########################
# Public Methods   
   def push(self, key):
      body = Node(key)
      body.next = head
      head = body
      return
   
   def pop(self, str):
      temp = head.key
      head = head.next
      return temp
   
   def peek(self):
      return head
      
   def dump(self):
     temp = head;
     while (temp != null):
       print(temp.key);
       temp = temp.next;
     return
   
   def isEmpty(self):
      return (count == 0)

   def getLength(self):
      return count; 
   
# ###############################
# Sub-Class
class Node(Stack):
   # ###########################
   # Constructor
   def __init__ (self, key):
      self.key = key
      self.next = null
