class Queue:
# ######################################
# Class Variables
   private head = Node("")
   private tail
   private count

# ######################################
# Public Methods
   def enqueue(self, num):
      backOfLine = Node(num)
      if (isEmpty()):
         head = backOfLine
         tail = backOfLine      
       else:
         tail.next = backOfLine
         tail = backOfLine
      count += 1
      return
   

   def dequeue():
      if(!isEmpty()):
         if (count > 1):
            temp = head
            head = head.next
            temp.next = null
         else:
            head = null 
            tail = null
         count -= 1
      } return
   }

   def dump(self):
     temp = head;
     while (temp != null):
       print(temp.key)
       temp = temp.next
     return
   
   def isEmpty(self):
      return (count == 0)

   def getLength(self):
      return count
    
   def peek(self):
      return head

# ######################################
# Sub-Class
class Node(Queue):
   # #################################
   # Constructor
   Node (self, key):
      self.key = key
      self.next = null
