class convertToString:
	def __init__(self):
		self.convertString = "0123456789ABCDEF"
	def toStr(self,n,base):
		if n<base:
			return self.convertString[n]
		else:
			x = n/base
			y = n%base
			return self.toStr(x,base) + self.convertString[y] 




A = convertToString()
print(A.toStr(30,2))
