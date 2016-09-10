from stack import Stack
S = Stack()
def revString(mystr):
    cha = list(mystr)
    revstr = ""	
    for i in range(0,len(cha)):
	S.push(cha[i])
    while not S.isEmpty():
	revstr = revstr + S.pop()

    return revstr

print(revString("revstring"))			
