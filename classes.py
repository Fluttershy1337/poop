class Things:
	pass


class Animate(Things):
	pass


class Inanimate(Things):
	pass


class Sidewalks(Inanimate):
	pass


class Animals(Animate):
	def breathe(self):
		print("дышыт")


	def move(self):
		print("двигоетса")


	def eating(self):
		print("йест")


class Mammals(Animals):
	def feed_with_milk(self):
		print("кормит молоком дитей")


class Giraffes(Mammals):
	def eating_leaves(self):
		print("хавоет листеки")


	def find_food(self):
		self.move()
		print("йа нашол йеду)")
		self.eating()


	def dancing(self):
		self.move()
		self.move()
		self.move()
		self.move()


petya = Giraffes()

petya.move()

petya.eating_leaves()

petya.dancing()

vasya = Giraffes()

vasya.feed_with_milk()
