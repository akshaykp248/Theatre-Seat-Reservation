import os
def readFile(reservations):
	if os.path.exists(reservations):
		res = []
		with open(reservations) as file:
			temp = file.readlines()
		for i in temp:
			s = res.append(i.strip().split(" "))
		return res
	else:
		raise Exception("Invalid input path")