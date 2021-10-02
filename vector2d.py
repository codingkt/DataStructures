from __future__ import annotations
from math import atan2, sqrt


class Vector2D:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	@property
	def length(self):
		return sqrt((self.x ** 2) + (self.y ** 2))
		
	@property
	def arg(self):
		return atan2(self.y, self.x)

	def dot(self, other: Vector2D):
		return (self.x * other.x) + (self.y * other.y)

	def __add__(self, other: Vector2D):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __sub__(self, other: Vector2D):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __mul__(self, factor: float):
		return Vector2D(self.x * factor, self.y * factor)

	__rmul__ = __mul__

	def __truediv__(self, factor: float):
		return Vector2D(self.x / factor, self.y / factor)

	def __floordiv__(self, factor: float):
		return Vector2D(self.x // factor, self.y // factor)

	def __pow__(self, power: float):
		return Vector2D(self.x ** power, self.y ** power)

	def __repr__(self):
		return 'Vector2D({}, {})'.format(self.x, self.y)
