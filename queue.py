class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, e):
		self.items.append(e)

	def dequeue(self):
		if len(self.items) > 0:
			return self.items.pop(0)
	
	def front(self):
		if len(self.items) > 0:
			return self.items[0]

	def back(self):
		if len(self.items) > 0:
			return self.items[-1]

	def empty(self):
		return len(self.items) == 0
