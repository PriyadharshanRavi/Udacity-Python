class Enemy:

	def __init__(self, energy):
		self.energy = energy

	def get_energy(self):
		print(self.energy)

Nambiyar = Enemy(5)
Raguvaran = Enemy(20)

Nambiyar.get_energy()
Raguvaran.get_energy()


