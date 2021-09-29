string = input()
cDict = {}

for i in string:
	if i not in cDict:
		cDict[i] = 1
	else:
		cDict[i] += 1

delete = 0
for count in cDict.values():
	if count % 2 != 0:
		delete += 1

if delete > 0:
	delete -= 1

print(delete)