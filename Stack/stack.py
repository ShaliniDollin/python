class Stack:
    def __init__(self):
	self.items = []
    def isEmpty(self):
 	return self.items == []
    def push(self,item):
	self.items.append(item)
    def pop(self):
	return self.items.pop()
    def size(self):
	return len(self.items)
    def peek(self):
	for i in range(0,self.size()):
	   print(self.items[i]) 		
