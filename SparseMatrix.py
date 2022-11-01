class SparseMatrix:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = {}

	def __getitem__(self, index):
		return self.data.get(index, 0)

	def __setitem__(self, index, value):
		self.data[index] = value

	def __add__(self, other):
		assert self.rows == other.rows and self.cols == other.cols

		result = SparseMatrix(self.rows, self.cols)
		for index in self.data:
			result[index] = self[index]
		for index in other.data:
			result[index] += other[index]
		return result

	def __mul__(self, other):
		assert self.cols == other.rows

		result = SparseMatrix(self.rows, other.cols)
		for i in range(self.rows):
			for j in range(other.cols):
				for k in range(self.cols):
					result[i, j] += self[i, k] * other[k, j]
		return result

	def __str__(self):
		result = []
		for i in range(self.rows):
			for j in range(self.cols):
				result.append(str(self[i, j]).rjust(8))
			result.append("\n")
		return ''.join(result)
