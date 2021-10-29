import math

def square(number):
	squared = math.sqrt(number)
	if squared == int(squared):
		return int(squared)
	else:
		return int(squared) + 1

def createMatrix(message, m):
	matrix = []
	for i in range(m):
		matrix.append([])
		for j in range(m):
			if len(message) > 0:
				matrix[i].append(message.pop(0))
			else:
				matrix[i].append("*")
	return matrix

def rotateMatrix(message, m):
	newMessage = []
	for _ in range(m):
		newMessage.append([])

	for i in range(m):
		for j in range(m):
			newMessage[j].insert(0, message[i][j])

	return newMessage

def printMessage(messageMatrix, m):
	message = ''
	for i in range(m):
		for j in range(m):
			if messageMatrix[i][j] != "*":
				message += messageMatrix[i][j]
	return message

n = int(input())
for _ in range(n):
	message = list(input())
	m = square(len(message))
	matrix = createMatrix(message, m)
	rotatedMatrix = rotateMatrix(matrix, m)
	print(printMessage(rotatedMatrix, m))
	