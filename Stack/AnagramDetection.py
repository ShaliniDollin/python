#checkingOff each character
def checkingOff (str1, str2):
   if (len(str1) != len(str2)):
	return False
   cha1 = str1
   cha2 = list(str2)
   for i in range(0,len(cha2)):
	if cha2[i] in cha1:
	   cha1 = cha1.replace(cha2[i],"",1)
	else:
	   return False
   if len(cha1)==0:
	return True

print(checkingOff("guruiii","riuiugi")) 
print(checkingOff("madam","daamm")) 

def sortandcompare(str1,str2):
   if len(str1) != len(str2):
	return False
   cha1 = list(str1) 
   cha2 = list(str2) 
   cha1.sort()
   cha2.sort()
   pos = 0
   matches = True
   while pos<len(cha1) and matches:
	if cha1[pos] == cha2[pos]:
	   pos=pos+1
	else:
	   matches =False
   return matches



print(sortandcompare("dasc","ascd"))

