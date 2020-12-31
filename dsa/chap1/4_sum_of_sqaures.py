def sum_of_squares(n):
	sum = 0
	for i in range(n):
		sum = sum + (i**2)

	return sum

x = sum_of_squares(0)
print(x)