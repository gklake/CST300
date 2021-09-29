people,chicken = map(int, input().split())
difference = chicken - people
if(difference < 0):
	if(abs(difference) > 1):
		print("Dr. Chaz needs", abs(difference), "more pieces of chicken!")
	else:
		print("Dr. Chaz needs", abs(difference), "more piece of chicken!")
else:
	if(difference > 1):
		print("Dr. Chaz will have", difference, "pieces of chicken left over!")
	else:
		print("Dr. Chaz will have", difference, "piece of chicken left over!")