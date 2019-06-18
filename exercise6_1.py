orig = open("D:\\meow\\meowwork\\poop\\orig.txt",'w')
orig.write('здрасте тут капец важные данные пиздец аа')
orig.close()

orig = open("D:\\meow\\meowwork\\poop\\orig.txt")
data = orig.read()
orig.close()

copy = open("D:\\meow\\meowwork\\poop\\copy.txt",'w')
copy.write(data)
copy.close()

copy = open("D:\\meow\\meowwork\\poop\\copy.txt")
copied_data = copy.read()
copy.close()

print(copied_data)
