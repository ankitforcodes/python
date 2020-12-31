def is_even(k):
	a = 0
	for i in range(0, k+2, 2):
		print(i)
		a = i

	if a == k:
		return True

	return False

z = is_even(2)
print(z)