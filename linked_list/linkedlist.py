#linked list implementation
class node:
	def __init__(self,data):
		self.data = data
		self.next = None
	def getData(self):
		return self.data
	def setData(self,newData):
		self.data = newData
	def setNext(self,newNext):
		self.next = newNext
	def getNext(self): 
		return self.next


class unorderedlist:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		if self.head == None:
			return True
		return False
	def add(self,item):
		temp = node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		count = 0
		temp = self.head
		while temp != None:
			count = count + 1
			temp = temp.getNext()
		return count

	def search(self,item):
		temp = self.head
		while temp != None:
			if temp.getData() == item:
				return True
			else:
				temp = temp.getNext()
		return False		
	def remove(self,item):
		temp =self.head
		Found = False
		if temp.getData() == item:
			Found = True
			now = temp.getNext()
			if now != None:
				self.head = now
			else:
				self.head = None
		prev = temp
		temp = temp.getNext()
		while temp != None and Found is False:
			if temp.getData() == item:
				prev.next = temp.getNext()
				Found = True
			prev = temp
			temp = temp.getNext()
			
	def append(self,item):
		temp = self.head
		new = node(item)
		
		while temp.getNext() != None:
			temp = temp.getNext()
		temp.next = new

	def printlist(self):
		temp = self.head
		print("hello")
		while temp != None:
			print(temp.data)
			temp = temp.getNext()	
		
