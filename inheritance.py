class Parent():
	"""docstring for Parent"""
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	"""docstring for Child"""
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
						
james_bond=Parent("Bond", "brown")	
print(james_bond.last_name)

john_bond = Child("Bond","Brown",5)
print(john_bond.last_name)
print(john_bond.number_of_toys) 