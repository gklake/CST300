bAge, bRetire, bSave, aAge, aSave = map(int, input().split())

bobsRetireMoney = (bRetire - bAge) * bSave
alicesRetireMoney = 0

while (alicesRetireMoney <= bobsRetireMoney):
	aAge += 1
	alicesRetireMoney += aSave

print(aAge)


