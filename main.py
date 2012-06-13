import sip
sip.setapi('Qvariant', 2)
from PyQt4 import QtCore, QtGui
from ReaderWidget import QtReader
#from calibre_plugins.speed_reader.config import prefs


class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.textEdit = QtReader("this is a test".split(), 60)
		self.textEdit.setReadOnly(True)
		self.setCentralWidget(self.textEdit)
		self.pauseButton=QtGui.QPushButton("&Pause")
		self.goButton=QtGui.QPushButton("&go")
		self.createDock()
		self.textEdit.start()
	def createDock(self):
		tb = QtGui.QToolBar(self)
		tb.setWindowTitle("test")
		self.addToolBar(QtCore.Qt.BottomToolBarArea,tb)
		self.pauseButton.clicked.connect(self.pauseReader)
		self.pauseButton.show()
		self.pauseButton=tb.addWidget(self.pauseButton)
		tb.show()
		self.goButton.clicked.connect(self.startReader)
		self.goButton = tb.addWidget(self.goButton)
		self.goButton.setVisible(False)
	def pauseReader(self):
		self.textEdit.timer.stop()
		self.pauseButton.setVisible(False)
		self.goButton.setVisible(True)
		
	def startReader(self):
		self.textEdit.timer.start()
		self.goButton.setVisible(False)
		self.pauseButton.setVisible(True)
	
	

if __name__ =='__main__':

	import sys
	app = QtGui.QApplication(sys.argv)
	mainWin = MainWindow()

	mainWin.show()
	sys.exit(app.exec_())
