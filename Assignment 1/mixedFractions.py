while(True):
	numerator,denominator = map(int, input().split())
	if(numerator == 0 and denominator == 0):
		break
	else:
		wholeNum = numerator // denominator
		remainder = numerator % denominator
		print(wholeNum, remainder, "/", denominator)
