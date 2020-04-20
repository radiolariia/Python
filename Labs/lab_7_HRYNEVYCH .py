import random

def genMatrix(row, col):
	matrix = []
	for i in range(row):
		matrix.append([])
		for j in range(col):
			matrix[i].append(random.randint(0, 10))
	return matrix

def transpose(matrix):
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for row in rez:
        return row


n = int(input('Enter n: '))
m = int(input('Enter m: '))

matrix = genMatrix(n, m)
print(matrix)
print(transpose(matrix))
