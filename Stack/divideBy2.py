#convert Decimal Number to Binary number
from stack import Stack
def divideby2(Num):
   s = Stack()
   if Num<1:
      return Num
   while Num > 0:
      rem = Num % 2
      s.push(rem)
      Num = Num/2
   binS = "" 
   while not s.isEmpty():
      binS = binS + str(s.pop())

   return binS    

print(divideby2(48)) 
print(divideby2(25))


def BaseConverter(Num,base):
    digits = "0123456789ABCDEF"
    s = Stack()
    if Num<1:
       return Num
    while Num>0:
       rem = Num % base
       s.push(rem)
       Num = Num/base
    binS = ""
    while not s.isEmpty():
       binS = binS + digits[s.pop()]

    return binS

print(BaseConverter(25,2)) 		
print(BaseConverter(25,6))
print(BaseConverter(25,16)) 	
print(BaseConverter(25,8)) 	
print(BaseConverter(256,16)) 	
print(BaseConverter(26,26)) 	
	
