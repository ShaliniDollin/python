class revString:
	def reverse(self,string1):
		if len(string1)<2:
			return string1
		else:
			return string1[-1] + self.reverse(string1[:-1])

	def isPalindrome(self,string1):
		if string1.lower() == self.reverse(string1).lower():
			return True
		return False
A = revString()
print("live",A.reverse("live"))
print("please",A.reverse("please"))
print("please",A.isPalindrome("please"))
print("kayak",A.isPalindrome("kayak"))
print("Kayak",A.isPalindrome("Kayak"))
