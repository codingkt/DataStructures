class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, e):
		self.items.append(e)

	def pop(self):
		if len(self.items) > 0:
			return self.items.pop()
	
	def top(self):
		if len(self.items) > 0:
			return self.items[-1]

	def empty(self):
		return len(self.items) == 0
