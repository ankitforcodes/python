def odd_squared(n):
	total = 0
	for i in range(n):
		if i%2 != 0:
			total = total + i**2

	return total


x = odd_squared(4)
print(x)