print(abs(-666))
print(abs(-70))
steps = -3
if abs(steps) > 0:
	print('пэрсонаж двигоется')

print(bool(0))
print(bool(1))
print(bool(666))

print(bool(""))
print(bool("лол"))

print(bool({}))
print(bool(bool))

year = input("введите год своево рождения пожалуйста: ")
if not bool(year.rstrip()):
	print('сука ну введи')

popcorn = 'строчка лол'
dir(popcorn)
help(popcorn.upper)
popcorn.upper()

eval("print('я удалю всю твою систему к чёртовой матери ты слышиш?')")
exec("print('я тоже удолю слышиш?')")

float('12')
float('12.34748')

int(123.555)
int('123')

max(80, 90, 75)
max('ГовНо')

min(80, 87, 38)
min('НегОвно')

list_of_numbers = list(range(0, 500, 50))
print(list_of_numbers)
print(sum(list_of_numbers))

test_text = open('D:\\meow\\meowwork\\poop\\test.txt')
text = test_text.read()
print(text)
test_text.close()

test_file = open('D:\\meow\\meowwork\\poop\\my_file.txt', 'w')
test_file.write('я всё ещё пидор')
test_file.close()


