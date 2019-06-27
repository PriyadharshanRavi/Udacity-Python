class Parent():

	def lastname(self):
		print("Ravi")

class Child(Parent):

	def firstname(self):
		print("Priyadharshan")
	
	def lastname(self): #override
		print("kingmaker")	

Priyadharshan = Child()
Priyadharshan.firstname()
Priyadharshan.lastname()


