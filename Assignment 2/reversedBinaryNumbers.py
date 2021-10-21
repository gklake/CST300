n = int(input())
reverse = 0

# traversing bits of the user's number from the right
while(n > 0):
	# using bitwise left shift by 1
	reverse = reverse << 1

	# checking if the current bit is 1
	if(n & 1 == 1):
		reverse = reverse ^ 1
		
	# using bitwise right shift by 1
	n = n >> 1

print(reverse)
