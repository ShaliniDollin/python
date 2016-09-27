class List1:
	def __init__(self):
		self.list1 = []
	def add(self,item):
		self.list1.append(item)
	def remove(self,item):
		self.list1.remove(item)
	def search(self,item):
		for i in self.list1:
			if i == item:
				return True
		return False
	def isEmpty(self):
		length = len(self.list1)
		if length == 0:
			return True
		return False
	def size(self):
		length = len(self.list1)
		return length
	def append(self,item):
		self.list1.append(item)
	def index(self,item):
		for i in range(0,len(self.list1)):
			if self.list1[i] == item:
				return i
		return None
	def insert(self,pos,item):
		if len(self.list1)<pos:
			return None
		self.list1.insert(pos,item)
	def pop(self,i=-1):
		a = self.list1[i]
		del self.list1[i]
		return a

	def peek(self):
		print(self.list1)
