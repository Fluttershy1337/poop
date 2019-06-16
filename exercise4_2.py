from sys import stdin


def read(fuckninput):
	try:
		print(fuckninput)
		return int(stdin.readline())
	except Exception:
		return read(fuckninput)



def moon():
	year = read('скоко годикоф раститывать?')
	weight = read('ваш вес?')
	increase = read('на скоко вы талстее за годек?')
	for i in range(year):
		print('твой лунный вес в %s году = %s' % (i + 1, weight * 0.165))
		weight = weight + increase


moon()
