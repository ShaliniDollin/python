# first in first out
# Addition at one end called rear 
# removal at other end called front
class Queue:
   def __init__(self):
	self.items = []
   def enqueue(self,item):
	self.items.append(item)
   def dequeue(self):
	if len(self.items)>0:
	     a = self.items[0]
	     del self.items[0]
	     return a 
	else:
	     print("List is empty")	
	
   def isEmpty(self):
	if len(self.items)<1:
		return True
	return False
   def size(self):
	return len(self.items)
   def peek(self):
	print(self.items)
