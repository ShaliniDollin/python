#paranthesis checker - to check is String has balanced paranthesis
from stack import Stack
#only symbol used in the function is "("
def parChecker(Symbol):
   if len(Symbol)<1:
	raise ValueError("Empty string")
   s = Stack()
   Balanced = True
   index = 0	
   Symbol = list(Symbol)	
   while index<len(Symbol) and Balanced:
      if Symbol[index] == "(":
	s.push(Symbol[index])
      else:
	if s.isEmpty():
	   Balanced = False
	else:
	   s.pop()
      index = index + 1
   if Balanced and s.isEmpty():
	return Balanced
   else:
	return False
 	  	
print(parChecker("((()(())))"))
print(parChecker("((()"))
print(parChecker("()"))
     	 
#{[()]} 
#now we should even check he order of appearence
#{[(])} -  is not valid
def parCheck2(Symbol):
   if len(Symbol)<1:
	raise ValueError("Empty String")
   sym = list(Symbol)
   balanced = True
   index = 0 
   s = Stack() 
   while index < len(sym) and balanced:
      if sym[index] in "[{(":
          s.push(sym[index])
      else:
	  if s.isEmpty():
	     balanced = False
          else:
             top = s.pop()
             balanced = matchesOrder(top,sym[index])
      index = index + 1           	
   if balanced and s.isEmpty():
	return balanced
   else:
        return False

def matchesOrder(open,close):
   opens = "{[("
   closes = "}])"
   try:
	return opens.index(open) == closes.index(close)
   except:
        raise ValueError("Not a valid symbol")

	
print(parCheck2("{[]{()}[]}"))		
print(parCheck2("{[])}[]"))		
      
  	
