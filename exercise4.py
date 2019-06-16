def moon(weight, increase):
	for i in range(1,16):
		print('твой лунный вес в %s году = %s' % (i, weight * 0.165))
		weight = weight + increase


moon(70, 1)
