from __future__ import annotations

class Bitset:
	def __init__(self, length: int, zero: bool = True):
		self.length = length
		bit = False if zero else True
		self.bits = [bit for _ in range(self.length)]

	@property
	def value(self):
		return int(self.__bitstring(), 2)

	def is_set(self, pos: int):
		return self.bits[pos]

	def set(self, pos: int):
		self.bits[pos] = True

	def set_all(self):
		for i in range(self.length):
			self.bits[i] = True
	
	def unset(self, pos: int):
		self.bits[pos] = False

	def unset_all(self):
		for i in range(self.length):
			self.bits[i] = False

	def flip(self, pos: int):
		self.bits[pos] = not self.bits[pos]

	def flip_all(self):
		for i in range(self.length):
			self.bits[i] = not self.bits[i]
	
	def __getitem__(self, pos: int): return 1 if self.bits[pos] else 0

	def __eq__(self, other: Bitset): return self.bits == other.bits

	def __and__(self, other: Bitset): return self.__combine(other, '__and__')
	
	def __or__(self, other: Bitset): return self.__combine(other, '__or__')
	
	def __xor__(self, other: Bitset): return self.__combine(other, '__xor__')

	def __invert__(self):
		b = Bitset(self.length)
		for i in range(self.length):
			b.bits[i] = not self.bits[i]
		return b

	def __combine(self, other: Bitset, op: str):
		assert(self.length == other.length)
		b = Bitset(self.length)
		for i in range(self.length):
			b.bits[i] = getattr(self.bits[i], op)(other.bits[i])
		return b

	def __bitstring(self, reverse: bool = True):
		if reverse:
			return ''.join(['1' if self.bits[i] else '0' for i in range(self.length-1, -1, -1)])

		return ''.join(['1' if self.bits[i] else '0' for i in range(0, self.length)])

	def __repr__(self):
		return 'Bitset({})'.format(self.__bitstring())
