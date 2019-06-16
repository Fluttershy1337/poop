ingridients = ['кузя', 'катик', 'gaytest.py', 'love', 'pussy']
number = 1

print("список индгридиентс фор гейсех: ")

for i in ingridients:
	print("%s. %s" % (number, i))
	number += 1

print("список индгридиентс фор гейсех2.0: ")
	
for i in range(len(ingridients)):
	print('%s. ' % (i + 1) + ingridients[i])
