from time import asctime
from sys import stdin


read = stdin.readline

def building(cans):
    total_cans = 0
    for week in range(53):
            if week == 0:
                    continue
            total_cans = total_cans + cans
            print('week %s, cans %s' % (week, total_cans))
            

building(3)

print(asctime())

def question(age):
	if age == 10:
		print('тебе 10 лет лол')
	else: 
		print('бля тебе не 10 лет лол')


question(int(read()))
