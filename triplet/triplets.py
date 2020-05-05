class Triplets:

	def __init__(self, entry1, entry2):
		self.entry1 = entry1
		self.entry2 = entry2
		self.length = len(entry1)
		self.score = [0,0]

		if self.length != 3:
			raise Exception('Bad data size')
		
		for element in self.entry1:
			if not (1 <= element <= 100):
				raise Exception('Data out of range')
		for element in self.entry2:
			if not (1 <= element <= 100):
				raise Exception('Data out of range')
		
	def review(self):
		for challenge in range(self.length):
			if self.entry1[challenge] > self.entry2[challenge]:
				self.score[0] = self.score[0] + 1
			if self.entry1[challenge] < self.entry2[challenge]:
				self.score[1] = self.score[1] + 1