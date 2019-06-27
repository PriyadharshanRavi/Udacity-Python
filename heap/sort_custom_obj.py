from operator import attrgetter

class User:

	def __init__(self, x,y):
		self.name = x
		self.id = y

	def __repr__(self):
		return self.name + " : " + str(self.id)	


users = [
	User('Priyan', 23),
	User('Archu', 22),
	User('Dhanam', 40),
	User('Kaviya', 18)
]		

for user in users:
	print(user)

print("____________________________________________\n")

for user in sorted(users, key = attrgetter('name')):
	print(user)

print("____________________________________________\n")

for user in sorted(users, key = attrgetter('id')):
	print(user)
