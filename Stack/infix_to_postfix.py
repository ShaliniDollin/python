from stack import Stack

def infix_to_postfix(exp):	
    BODMAS = {}
    BODMAS['/'] = 3	
    BODMAS['*'] = 3	
    BODMAS['+'] = 2	
    BODMAS['-'] = 2	
    BODMAS['('] = 1	
    output = []
    opstack = Stack()
    infix = list(exp)
    print(exp)	
    for x in infix:
	if x == "(":
	    opstack.push(x)
	elif x == ")":
	    flag = True	
	    while flag:
		op = opstack.pop()
		if op == "(":
		    flag = False
		else:
		    output.append(op)
	elif x in BODMAS:
	    if not opstack.isEmpty():	
 	    	op = opstack.pop()
	    	if BODMAS[x] <= BODMAS[op]:
	       	    output.append(op)
	        else:
		    opstack.push(op)		 				
	    opstack.push(x)	
	else:
	    output.append(x)
    while not opstack.isEmpty():
	op = opstack.pop()
	if op is not "(":
	    output.append(op)
    out =''.join(output)
    return out

print(infix_to_postfix("(A+B)*C"))
print(infix_to_postfix("A*B+C*D"))
print(infix_to_postfix("(A+B)*C-(D-E)*(F+G)"))
			 				
	     
	
