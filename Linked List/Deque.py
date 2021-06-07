class Deque:
# ######################################
# Class Variables
   head = Node("")
   tail = Node()
   count = 0

# ######################################
# Public Methods
   def enqueue(self, key):
      backOfLine = Node (key)
      if (isEmpty()):
         head = backOfLine
         tail = backOfLine      
      else:
         tail.next = backOfLine
         tail = backOfLine
      count += 1
      return

   def push(String str):
      body = Node(str);
      body.next = head
      head = body
      return

   def pop():
      temp = head.key
      head = head.next
      return temp
   
   def isEmpty():
      return (count == 0)

   def peek():
      if (!isEmpty()): 
         return head
      
# ######################################
# Sub-Class
class Node(Deque):
   # #################################
   # Constructor
   Node (self, string):
      self.key = key
      next = null
