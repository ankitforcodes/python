class Flower():
	def __init__(self, name, petals, price):
		self.name = str(name)
		self.petals = int(petals)
		self.price = float(price) 

	def setName(self, name):
		self.name = name

	def setPetals(self, petals):
		self.petals = petals

	def setPrice(self, price):
		self.price = price


	def getName(self):
		return self.name

	def getPetals(self):
		return self.petals

	def getPrice(self):
		return self.price