try:
	money = int(input("скоко у тибя денек? "))

	if money in range(100,501) or money in range(1000,5001):
		print("у вас или от сотки до пятиста или от косаря до 5к денек) хз зачем вам ета инфа")
	else:
		print("я хз скоко у тибя денек")
except Exception:
	print("ты фсё сломал(")
			 