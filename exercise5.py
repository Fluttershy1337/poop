class Giraffes:
	def __init__(self, pidorstvo):
		self.level_pidorstva = pidorstvo


	def left_foot_forward(self):
		print("левая нога ебаного жирафа впереди")


	def right_foot_forward(self):
		print("правая нога ебаного жирафа впереди")


	def left_foot_back(self):
		print("левая нога ебучего жирафа сзади")


	def right_foot_back(self):
		print("правая нога ебучего жирава сзади")


	def dance(self):
		self.right_foot_back()
		self.left_foot_forward()
		self.left_foot_back()
		self.right_foot_forward()
		self.right_foot_back()
		self.left_foot_back()
		print('и он наебнулся, конец^^')


vasya = Giraffes(100)

print(vasya.level_pidorstva)

vasya.dance()

