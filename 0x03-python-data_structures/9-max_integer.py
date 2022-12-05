def max_integer(my_list=[]):
	largest = my_list[0]
	for item in my_list:
		if item >= largest:
			largest = item
	return largest
