class MatrixOperations:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def constructMatrix(self):
		print("Enter elements one by one row wise: ")
		resultMat =[]
		for i in range(self.row):
			rowElm = []
			for j in range(self.col):
				print(f"Enter the element ({i+1}, {j+1}) = ",end="")
				element = int(input())
				rowElm.append(element)
			resultMat.append(rowElm)
		return resultMat

	def sumMatrix(self, matrix_A, matrix_B):
		resultSum = []
		for i in range(len(matrix_A)):
			rowElm = []
			for j in range(len(matrix_B)):
				resutlElm = matrix_A[i][j] + matrix_B[i][j]
				rowElm.append(resutlElm)				
			resultSum.append(rowElm)
		return resultSum

	def subtMatrix(self, matrix_A, matrix_B):
		resultSubt = []
		for i in range(len(matrix_A)):
			rowElm = []
			for j in range(len(matrix_B)):
				resutlElm = matrix_A[i][j] - matrix_B[i][j]
				rowElm.append(resutlElm)				
			resultSubt.append(rowElm)
		return resultSubt

	def multMatrix(self, matrix_A, matrix_B):
		resultMult = []
		for i in range(len(matrix_A)):
			rowElm = []
			for j in range(len(matrix_B[0])):
				sop = 0
				for k in range(len(matrix_A[0])):
					sop = sop + matrix_A[i][k] + matrix_B[k][j]
				rowElm.append(sop)
			resultMult.append(rowElm)
		return resultMult


if __name__ == "__main__":

	m, n = 2, 2 # order of the matrix
	operation = MatrixOperations(m, n)

	# creating matrices
	matrix1 = operation.constructMatrix()
	matrix2 = operation.constructMatrix()
	
	# basic operations
	addition = operation.sumMatrix(matrix1, matrix2)
	subtraction = operation.subtMatrix(matrix1, matrix2)
	multiplication = operation.multMatrix(matrix1, matrix2)
	print(f"\n\taddition: {addition}\n\tsubtraction: {subtraction}\n\tmultiplication: {multiplication}")
