def minmax(num_list):
	min_num =  num_list[0]
	max_num = num_list[0]

	for nums in num_list:
		if nums > max_num:
			max_num = nums

		if nums < min_num:
			min_num = nums

	return (min_num, max_num)

x,y = minmax([-1, 100, 50, 2, -18])
print(x,y)