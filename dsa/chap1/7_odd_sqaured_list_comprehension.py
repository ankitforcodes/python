def odd_squared(n):
	list_squared = [i**2 for i in range(n) if i%2 != 0]
	return sum(list_squared)

x = odd_squared(6)
print(x)