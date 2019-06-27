class Car:

	def hatchback(self, brand, price):
		self.brand = brand
		self.price = price
		print(self.brand + " is the brand name and it costs around " + self.price )
	def sedan(self, brand, price):	
		self.brand = brand
		self.price = price
		print(self.brand + " is the brand name and it costs around " + self.price )

brio = Car()
city = Car()

brio.hatchback("Honda", "5L")
city.sedan("Honda", "10L")