class Player:
	job = 'football player'

	# name = ''
	# speed = ''

	def __init__(self, nama, kecepatan):
		self.name = nama
		self._age = 23
		self.__age = 21
		self.speed = kecepatan

	def getName(self):
	# def getName(self, nama):
		# self.name = nama
		return self.name

	def getSpeed(self):
		return self.speed

	def getSkill(self):
		return 'normal'

	def getAge(self):
		return self.__age

	
	@staticmethod
	def retiredIn(age):
		return str(40 - age)

	@classmethod
	def generalInfo(cls, age):
		return cls.job + ' akan pensiun dalam ' + cls.retiredIn(age) + ' tahun'

	@property
	def infoPlayer(self):
		return self.name + " kecepatan nya " + self.speed
	
	@infoPlayer.setter
	def infoPlayer(self, data):
		name, speed = data.split(' ')
		self.name = name
		self.speed = speed


class MalaysiaPlayer(Player):
	pass

class IndonesiaPlayer(Player):
	def __init__(self, nama, kecepatan):
		# Player.__init__(self, nama, kecepatan)
		super().__init__(nama, kecepatan)
		print("hello indonesia")

	def getSkill(self):
		return 'drama'


# pemain = Player()
# print(pemain.getName('asd'))
# print(Player().getName('dsa'))

# player = Player('Epank', '20')
# player2 = Player('Dsa', '30')
# print(player.getName() + " Punya Speed " + player.getSpeed())
# print(player2.getName() + " Punya Speed " + player2.getSpeed())

# player = IndonesiaPlayer('Epank', '20')
# print(player.getName() + " umurnya " + player.setAge('22'))

# player = IndonesiaPlayer('Epank', '20')
# print(player.getName() + " skillnya " + player.getSkill())

# player = MalaysiaPlayer('Epank', '20')
# print(player.getName() + " skillnya " + player.getSkill())

# player = IndonesiaPlayer('Epank', '20')
# print(player.getName() + " skillnya " + player.getSkill())

# print(Player('Epank', '20')._age)
# print(Player('Epank', '20').getAge())

# print("Pensiun dalam " + Player.retiredIn(18) + " tahun")
# print(Player.generalInfo(30))


player = Player('Epank', '20')

print(player.infoPlayer)

player.infoPlayer = 'Ervan 21'
print(player.infoPlayer)