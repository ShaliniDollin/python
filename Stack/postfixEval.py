from stack import Stack

def postfixEval(exp):
    #list1 = list(exp)
    list1 = exp.split()
    print(list1)	
    if len(list1)<1:
	return list1
    opstack = Stack()
    for x in list1:
	try:
	    x = int(x)
	    if isinstance(x,int):
  	     	opstack.push(int(x))
	except:
	    if x in ('*','-','+','/'):
	        if not opstack.isEmpty():
		   op2 = opstack.pop()
	    	if not opstack.isEmpty():
		   op1 = opstack.pop()
	        if op1 and op2:
		   if x == "*":
		       ev = op1 * op2
		   elif x == "-":
		       ev = op1 - op2			
		   elif x == "+":
		       ev = op1 + op2	
		   else:
		       ev = op1/op2
		   opstack.push(int(ev))
	        else:
		   raise ValueError ("Not valid postfix")
	    else:
	        raise ValueError ("Not valid postfix")
    if not opstack.isEmpty():
	op = opstack.pop()
	if not opstack.isEmpty():
	    raise ValueError ("Not valid postfix")
	else:
	    return op	
    else:
	raise ValueError ("Not valid postfix")
		

print(postfixEval("4 5 6 * +"))
print(postfixEval("7 8 + 3 2 + /"))
print(postfixEval("17 10 + 3 * 9 /"))
		
