from stack import Stack

S = Stack()

print(S.isEmpty())
S.push(4)
S.push("Dog")
S.push("Cat")
S.push(3)
S.push("hello")
S.peek()
print(S.size())
print(S.pop())
print(S.size())
print(S.pop())

