class Mario():

	def move(self):
		print("I'm moving")

class Mushroom():

	def eat_mushroom(self):
		print("Now I'm big")
		
class Bigmario(Mario, Mushroom):
	pass

Player = Bigmario()
Player.move()
Player.eat_mushroom()	

	
		