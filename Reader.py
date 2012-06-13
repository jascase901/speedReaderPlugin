
class Reader(list):
	def __init__(self, wordLi,spot, wpm):
		list.__init__(self, wordLi)
		self.spot = spot
		self.wpm = wpm

		self.paused=False
		self = wordLi
	def next(self):
		if self.spot<len(self)-1:
			self.spot +=1
		else:
			self.paused=True
			print("max")
	def prev(self):
		if self.spot>0:
			self.spot -=1
		else:
			self.paused = True
			print("min")
	def getWord(self):
		return self[self.spot]
	
if __name__ == '__main__':
	reader = Reader(["he","yo"] , 0, 60)
	
	print(reader.getWord())
	reader.next()
	print(reader.getWord())
	reader.next()
	print(reader.getWord())
	reader.next()
	print(reader.getWord())
	reader.prev()
	print(reader.getWord())
	reader.prev()
	print(reader.getWord())
	reader.prev()
	print(reader.getWord())
	print("hello")

