import sip
from time import sleep
sip.setapi('Qvariant', 2)
from Reader import Reader
from PyQt4 import QtCore, QtGui 

class QtReader(QtGui.QTextEdit):
	def __init__(self, wordLi, wpm):
		super(QtReader, self).__init__() 
		self.setReadOnly(True)
		self.reader =Reader(wordLi, 0, 600);
		self.timer=QtCore.QTimer(self)
		self.timer.timeout.connect(self.flashWord)
		self.wpm = wpm
	
	def flashWord(self):
			if not self.reader.paused:
				self.setText(self.reader.getWord())
				self.reader.next()
	def start(self):
		self.timer.start(self.wpm/60*1000)
	def stop(self):
		self.timer.stop()

if __name__=='__main__':
	reader = QtReader("this is a test".split(), 60)
	print("readerWidget")
