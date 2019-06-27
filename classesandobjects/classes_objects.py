class Hero:
	life = 3

	def attack(self):
		print("Ouch!")
		self.life-=1
	def checklife(self):
		if self.life <= 0:
			print("you are dead")
		else:
			print((str(self.life)) + ' life left' )

vijaysethupathi = Hero()

vijaysethupathi.attack()
vijaysethupathi.attack()
vijaysethupathi.attack()
vijaysethupathi.attack()
vijaysethupathi.checklife()					 