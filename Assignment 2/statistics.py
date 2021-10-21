import sys

caseNum = 1
for i in sys.stdin:
	
	# creating a list of all the numbers
	currentCase = list(map(int, i.split()))

	maximum = max(currentCase[1:])
	minimum = min(currentCase[1:])
	diff = maximum - minimum
	
	print("Case " + str(caseNum) + ":", minimum, maximum, diff)
	caseNum += 1
