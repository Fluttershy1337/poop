def moon(weight, increase, year):
	for i in range(year):
		print('твой лунный вес в %s году = %s' % (i + 1, weight * 0.165))
		weight = weight + increase


moon(70, 1, 20)
