class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, e):
		self.items.append(e)

	def pop(self):
		return self.items.pop()
	
	def top(self):
		if len(self.items) > 0:
			return self.items[-1]
