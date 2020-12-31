def is_multiple(n,m):
	try:
		a = n/m

		if n%m == 0:
			return True
		
		return False
	except ZeroDivisionError:
		print("Cannot divide by 0")

x = is_multiple(4,1)
print(x)

x = is_multiple(4,0)
print(x)
