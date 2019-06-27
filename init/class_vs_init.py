
class Girl:

	gender = "female" #this variable is common to all the functions under this class
	def __init__(self, name):
		self.name = name # Anthing under a function is specific to that function
		print(self.name)

Girl1 = Girl("Rachel")
Girl2 = Girl("Angela")
print(Girl1.gender)
print(Girl2.gender)		


'''

class Hero:
	life = 5

	def being_attacked(self):
		print("otha!")
		self.life-=1

	def defence(self):
		print("otha saavu da pundha")
		self. life+=1	

	def checklife(self):
		if self.life <= 0:
			print("enaya savadichutiye da pundha")
		else:
			print((str(self.life)) + " life iruku.. naan Vizhven endru ninaithayo.. argh.. ")

class Villain:
	vlife = 3

	def villain_attacked(self):
		print("otha en melaye kaiya vachutiya?")
		self.vlife-=1
	def villain_defence(self):
		print("gommale shaavu da")
		self.vlife+=1	
	def vchecklife(self):
		if self.vlife<=0:
			print("enaye shavadichutiya")
		else:
			print((str(self.vlife)) + " life iruku... marubadiyum varuven")		



mgr = Hero()
nambiyar = Villain()


mgr.being_attacked()
mgr.being_attacked()

mgr.checklife()

nambiyar.villain_attacked()
nambiyar.villain_attacked()
nambiyar.villain_attacked()

nambiyar.vchecklife()

'''








