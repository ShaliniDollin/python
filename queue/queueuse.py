from queue import Queue
q = Queue()
q.enqueue(2)
q.enqueue("lesly")
print(q.size())
q.enqueue(3)
q.peek()
print(q.dequeue())
q.peek()
q.enqueue(12)
q.peek()
print(q.isEmpty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())
q.dequeue()
